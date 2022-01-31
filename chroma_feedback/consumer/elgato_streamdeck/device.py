from typing import Any, List
import copy
import webbrowser
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QBrush, QColor, QFont, QPainter, QPen, QPixmap, QTransform
from chroma_feedback import color, reporter
from chroma_feedback.typing import Consumer, ProducerReport, Status


def get_devices(devices : Any, device_names : List[str]) -> Any:
	if device_names:
		for device in copy.copy(devices):
			if device.id() not in device_names:
				devices.remove(device)
	return devices


def process_devices(devices : Any, producer_report : List[ProducerReport]) -> List[Consumer]:
	result : List[Consumer] = []
	status : Status = reporter.resolve_report_status(producer_report)

	# process device

	for device in devices:
		if set_device(device, producer_report):
			result.append(
			{
				'name': 'elgato_streamdeck',
				'type': 'device',
				'description': device.id(),
				'status': status
			})
	return result


def set_device(device : Any, producer_report : List[ProducerReport]) -> bool:
	device.open()
	device.reset()

	# process producer

	for index, value in enumerate(producer_report):
		if index < device.key_count():
			device.set_key_image(index, create_image(device, value['status']))
			if 'url' in value and value['url']:
				device.set_key_callback(lambda __checked__, url = value['url'] : webbrowser.open(url))

	# close device

	device.close()
	return device.is_open() is False


def create_image(device : Any, status : Status) -> Any:
	color_config = color.get_by_status(status)
	image_config = device.key_image_format()
	transform = create_transform(image_config)
	pixmap = QPixmap(image_config['size'][0], image_config['size'][1])
	pixmap.fill(Qt.transparent)
	pen = QPen(Qt.white)
	font = QFont()
	font.setPointSize(12)
	font.setBold(True)
	ellipse_height = int(image_config['size'][0] * 0.2)
	ellipse_width = int(image_config['size'][1] * 0.2)
	ellipse_left = int(image_config['size'][0] / 2 - ellipse_height / 2)
	ellipse_top = int(image_config['size'][1] / 2 - ellipse_width / 2)
	painter = QPainter(pixmap)
	painter.setBrush(QBrush(QColor(color_config['rgb'][0], color_config['rgb'][1], color_config['rgb'][2]), Qt.SolidPattern))
	painter.drawEllipse(ellipse_left, ellipse_top + 20, ellipse_height, ellipse_width)
	painter.setPen(pen)
	painter.setFont(font)
	painter.drawText(QRect(0, -10, image_config['size'][0], image_config['size'][1]), Qt.AlignCenter, status.upper())
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


def pixmap_to_bytes(pixmap : QPixmap, image_config : Any) -> bytes:
	byte_array = QtCore.QByteArray()
	buffer = QtCore.QBuffer(byte_array)
	buffer.open(QtCore.QIODevice.WriteOnly)
	pixmap.save(buffer, image_config['format'])
	return byte_array.data()
