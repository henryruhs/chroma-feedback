import atexit
import copy
import webbrowser
from typing import Any, List

from PyQt5 import QtCore
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QColor, QFont, QPainter, QPen, QPixmap, QTransform

from chroma_feedback import color, helper, reporter
from chroma_feedback.typing import Consumer, ProducerReport, Status
from .api import get_api

DEVICES = None


def get_devices() -> Any:
	global DEVICES

	if not DEVICES:
		DEVICES = get_api().enumerate()
	return DEVICES


def filter_devices(devices : Any, device_ids : List[str]) -> Any:
	if device_ids:
		for device in copy.copy(devices):
			if device.id() not in device_ids:
				devices.remove(device)
	return devices


def process_devices(devices : Any, producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	# process devices

	for device in devices:
		if set_device(device, producer_report):
			result.append(
			{
				'name': 'elgato_streamdeck',
				'type': 'device',
				'description': helper.create_description(device.deck_type(), device.id()),
				'status': status
			})
	return result


def set_device(device : Any, producer_report : List[ProducerReport]) -> bool:
	device.open()

	# process report

	for index, report in enumerate(producer_report):
		if index < device.key_count():
			device.set_key_image(index, create_image(device, report))
			if 'url' in report and report['url']:
				device.set_key_callback(lambda __, key, state : state is True and webbrowser.open(producer_report[key]['url']))

	# smooth reset

	for index in range(len(producer_report), device.key_count()):
		device.set_key_image(index, None)

	# close on destroy

	atexit.register(lambda : device.close())
	return device.is_open() is True


def create_image(device : Any, report : ProducerReport) -> Any:
	color_config = color.get_by_status(report['status'])
	image_config = device.key_image_format()
	transform = create_transform(image_config)
	font_size = image_config['size'][1] / 8
	pixmap = QPixmap(image_config['size'][0], image_config['size'][1])
	pixmap.fill(Qt.transparent)
	painter = QPainter(pixmap)
	painter.setFont(create_font(font_size * 2.75, QFont.Normal))
	painter.setPen(QPen(QColor(color_config['rgb'][0], color_config['rgb'][1], color_config['rgb'][2])))
	painter.drawText(QRect(0, font_size * 1.25, image_config['size'][0], image_config['size'][1]), Qt.AlignCenter, report['symbol'])
	painter.setFont(create_font(font_size * 0.875, QFont.Bold))
	painter.setPen(QPen(Qt.white))
	painter.drawText(QRect(0, font_size * -2, image_config['size'][0], image_config['size'][1]), Qt.AlignCenter, report['name'].upper())
	painter.end()
	return pixmap_to_bytes(pixmap.transformed(transform), image_config)


def create_transform(image_config : Any) -> QTransform:
	transform = QTransform()

	if image_config['flip'][0] is True:
		transform.scale(-1, 1)
	if image_config['flip'][1] is True:
		transform.scale(1, -1)
	if image_config['rotation']:
		transform.rotate(image_config['rotation'])
	return transform


def create_font(font_size : int, font_weight : int) -> QFont:
	font = QFont()
	font.setPointSize(font_size)
	font.setWeight(font_weight)
	return font


def pixmap_to_bytes(pixmap : QPixmap, image_config : Any) -> bytes:
	byte_array = QtCore.QByteArray()
	buffer = QtCore.QBuffer(byte_array)
	buffer.open(QtCore.QIODevice.WriteOnly)
	pixmap.save(buffer, image_config['format'])
	return byte_array.data()
