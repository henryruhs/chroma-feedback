import threading
from PIL import Image
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
	icon.icon = Image.open('src/consumer/system_tray/icon.png')
	return icon


def run():
	threading.Thread(daemon = True, target = create_icon().run())
