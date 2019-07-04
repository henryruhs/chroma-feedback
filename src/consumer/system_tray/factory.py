from src import core, metadata, wording


def icon_factory():

	# handle import

	try:
		from pystray import Icon, Menu, MenuItem
	except ImportError:
		exit(wording.get('package_no').format('PYSTRAY') + wording.get('exclamation_mark'))

	# build icon

	instance = Icon(metadata.get('name') + ' ' + metadata.get('version'))
	instance.menu = Menu(
		MenuItem(wording.get('stop'), core.destroy)
	)
	instance.icon = image_factory([255, 255, 255])
	return instance


def image_factory(rgb):

	# handle import

	try:
		from PIL import Image, ImageDraw
	except ImportError:
		exit(wording.get('package_no').format('PIL') + wording.get('exclamation_mark'))

	# build image

	image = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
	draw = ImageDraw.Draw(image)
	draw.ellipse((20, 20, 80, 80), fill = (255, 255, 255), outline = (0, 0, 0))
	draw.ellipse((30, 30, 70, 70), fill = (rgb[0], rgb[1], rgb[2]))
	return image
