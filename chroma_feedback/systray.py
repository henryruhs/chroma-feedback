from typing import Any, List
import tempfile
import os
from PIL import Image, ImageDraw
from chroma_feedback import color, metadata, wording
try:
	import gi

	gi.require_version('Gtk', '3.0')
	gi.require_version('AppIndicator3', '0.1')

	from gi.repository import AppIndicator3, GdkPixbuf, Gtk
except (ImportError, ValueError):
	exit(wording.get('package_no').format('GIRL APPINDICATOR') + wording.get('exclamation_mark'))

SYSTRAY = None


def create(status : str, report : List[str]) -> None:
	global SYSTRAY

	if not SYSTRAY:
		icon_path = create_icon(status)
		SYSTRAY = AppIndicator3.Indicator.new(metadata.get('name') + ' ' + metadata.get('version'), icon_path, AppIndicator3.IndicatorCategory.APPLICATION_STATUS)
		SYSTRAY.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
		SYSTRAY.set_menu(create_menu(report))
	Gtk.main()


def update(status : str, report : List[str]) -> None:
	icon_path = create_icon(status)

	SYSTRAY.set_icon(icon_path)
	SYSTRAY.set_menu(create_menu(report))


def is_active() -> bool:
	global SYSTRAY

	return SYSTRAY is not None


def create_menu(report : List[str]) ->Gtk.Menu:
	menu = Gtk.Menu()

	# process report

	for message in report:
		menu.append(Gtk.MenuItem(message))
	if report:
		menu.append(Gtk.SeparatorMenuItem())

	# handle action

	item_about = Gtk.MenuItem(wording.get('about'))
	item_about.connect('activate', about)
	item_exit = Gtk.MenuItem(wording.get('exit'))
	item_exit.connect('activate', destroy)
	menu.append(item_about)
	menu.append(item_exit)
	menu.show_all()
	return menu


def create_icon(status : str) -> str:
	color_config = color.get_by_status(status)
	image = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
	draw = ImageDraw.Draw(image)
	draw.ellipse((20, 20, 80, 80), fill = (color_config['rgb'][0], color_config['rgb'][1], color_config['rgb'][2]))
	path = tempfile.mktemp('.png')
	image.save(path)
	return path


def about(menu_item : Any) -> None:
	logo = GdkPixbuf.Pixbuf.new_from_file_at_size(create_icon('passed'), 20, 20)
	about_dialog = Gtk.AboutDialog()
	about_dialog.set_program_name(metadata.get('name'))
	about_dialog.set_comments(metadata.get('description'))
	about_dialog.set_version(metadata.get('version'))
	about_dialog.set_website(metadata.get('url'))
	about_dialog.set_website_label(metadata.get('url'))
	about_dialog.set_logo(logo)
	about_dialog.present()


def destroy(menu_item : Any) -> None:
	print('\r' + wording.get('goodbye') + wording.get('exclamation_mark'))
	os._exit(0)
