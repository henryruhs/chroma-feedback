import threading
from .factory import icon_factory, image_factory

icon = None


def run():
	global icon

	icon = icon_factory()
	threading.Thread(daemon = True, target = icon.run())


def update(status):
	global icon

	if status == 'passed':
		icon.icon = image_factory([0, 255, 0])
	if status == 'process':
		icon.icon = image_factory([255, 255, 0])
	if status == 'errored':
		icon.icon = image_factory([0, 0, 0])
	if status == 'failed':
		icon.icon = image_factory([255, 0, 0])
