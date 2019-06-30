import threading
from PIL import Image, ImageDraw
from src import core, metadata, wording
try:
	from pystray import Icon, Menu, MenuItem
except ImportError:
	exit(wording.get('package_no').format('pystray') + wording.get('exclamation_mark'))

instance = None


def create_icon():
	global instance

	instance = Icon(metadata.get('name') + ' ' + metadata.get('version'))
	instance.menu = Menu(
		MenuItem(wording.get('stop'), core.destroy)
	)
	instance.icon = draw_image([255, 255, 255])
	return instance


def draw_image(rgb):
	image = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
	draw = ImageDraw.Draw(image)
	draw.ellipse((20, 20, 80, 80), fill = (255, 255, 255), outline = (0, 0, 0))
	draw.ellipse((30, 30, 70, 70), fill = (rgb[0], rgb[1], rgb[2]))
	return image


def run():
	threading.Thread(daemon = True, target = create_icon().run())


def update(status):
	global instance

	if status == 'passed':
		instance.icon = draw_image([0, 255, 0])
	if status == 'process':
		instance.icon = draw_image([255, 255, 0])
	if status == 'errored':
		instance.icon = draw_image([0, 0, 0])
	if status == 'failed':
		instance.icon = draw_image([255, 0, 0])
