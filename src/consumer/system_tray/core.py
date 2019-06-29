import threading
from PIL import Image, ImageDraw
from src import core, metadata, wording
try:
	from pystray import Icon, Menu, MenuItem
except ImportError:
	exit(wording.get('package_no').format('pystray') + wording.get('exclamation_mark'))

def create_icon():
	icon = Icon(metadata.get('name') + ' ' + metadata.get('version'))
	icon.menu = Menu(
		MenuItem(wording.get('stop'), core.destroy)
	)
	icon.icon = draw_image()
	return icon


def draw_image():
	image = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
	draw = ImageDraw.Draw(image)
	draw.ellipse((20, 20, 80, 80), fill = (255, 255, 255), outline = (0, 0, 0))
	return image


def run():
	threading.Thread(daemon = True, target = create_icon().run())
