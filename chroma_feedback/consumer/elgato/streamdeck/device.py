import atexit
import copy
from typing import Any, List

from PyQt6 import QtCore
from PyQt6.QtCore import QRect, Qt
from PyQt6.QtGui import QColor, QFont, QPainter, QPen, QPixmap, QTransform

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

	for device in devices:
		if set_device(device, producer_report):
			register_close_device(device)
			if helper.has_argument('-b') or helper.has_argument('--background-run'):
				register_reset_device(device)
			result.append(
			{
				'name': 'elgato.streamdeck',
				'type': 'device',
				'description': helper.create_description(device.deck_type(), device.id()),
				'status': status
			})
	return result


def set_device(device : Any, producer_report : List[ProducerReport]) -> bool:
	device.open()

	for index in range(device.key_count()):
		if device.KEY_PIXEL_HEIGHT > 0 and device.KEY_PIXEL_WIDTH > 0:
			if index < len(producer_report):
				device.set_key_image(index, create_image(device, producer_report[index]))
			else:
				device.set_key_image(index, None)

	return device.is_open()


def register_close_device(device : Any) -> None:
	atexit.register(lambda: device.close())


def register_reset_device(device : Any) -> None:
	atexit.register(lambda: device.reset())


def create_image(device : Any, report : ProducerReport) -> bytes:
	color_config = color.get_by_status(report['status'])
	image_config = device.key_image_format()
	transform = create_transform(image_config)
	font_size = image_config['size'][0] / 8
	pixmap = QPixmap(*image_config['size'])
	pixmap.fill(Qt.GlobalColor.transparent)
	painter = QPainter(pixmap)
	painter.setFont(create_font(int(font_size * 2.75), QFont.Weight.Bold))
	painter.setPen(QPen(QColor(*color_config['rgb'])))
	painter.drawText(QRect(0, int(font_size * 1.5), *image_config['size']), Qt.AlignmentFlag.AlignCenter, report['symbol'])
	painter.setFont(create_font(int(font_size * 0.875), QFont.Weight.Bold))
	painter.setPen(QPen(Qt.GlobalColor.white))
	painter.drawText(QRect(0, int(font_size * -1.875), *image_config['size']), Qt.AlignmentFlag.AlignCenter, report['name'].split('.')[-1].upper())
	painter.end()
	return pixmap_to_bytes(pixmap.transformed(transform), image_config)


def create_transform(image_config : Any) -> QTransform:
	transform = QTransform()

	if image_config['flip'][0]:
		transform.scale(-1, 1)
	if image_config['flip'][1]:
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
	buffer.open(QtCore.QIODevice.OpenModeFlag.WriteOnly)
	pixmap.save(buffer, image_config['format'])
	return byte_array.data()
