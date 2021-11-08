import sys
from typing import List
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush, QIcon, QPainter, QPixmap
from PyQt5.QtWidgets import QMenu, QSystemTrayIcon
from chroma_feedback import color, loop, wording
from chroma_feedback.typing import Status, Report

SYSTRAY = None
MENU = None


def create(status : Status, report : List[Report]) -> None:
	global SYSTRAY, MENU

	if not SYSTRAY:
		SYSTRAY = QSystemTrayIcon()
	if not MENU:
		MENU = QMenu()
	update(status, report)
	SYSTRAY.show()


def update(status : Status, report : List[Report]) -> None:
	global SYSTRAY, MENU

	update_menu(report)
	SYSTRAY.setContextMenu(MENU)
	SYSTRAY.setIcon(create_icon(status))


def is_created() -> bool:
	global SYSTRAY, MENU

	return SYSTRAY is not None and MENU is not None


def update_menu(report : List[Report]) -> None:
	global MENU

	MENU.clear()

	# process report

	for value in report:
		item_report = MENU.addAction(value['message'])
		item_report.setIcon(create_icon(value['status']))
		item_report.setIconVisibleInMenu(True)
	if report:
		MENU.addSeparator()

	# handle action

	item_start = MENU.addAction(wording.get('start'))
	item_start.triggered.connect(action_start)
	MENU.addAction(item_start)
	item_stop = MENU.addAction(wording.get('stop'))
	item_stop.triggered.connect(action_stop)
	MENU.addAction(item_stop)
	item_exit = MENU.addAction(wording.get('exit'))
	item_exit.triggered.connect(action_exit)
	MENU.addAction(item_exit)


def create_icon(status : Status) -> QIcon:
	color_config = color.get_by_status(status)
	pixmap = QPixmap(100, 100)
	pixmap.fill(Qt.transparent)
	painter = QPainter(pixmap)
	painter.setBrush(QBrush(QColor(color_config['rgb'][0], color_config['rgb'][1], color_config['rgb'][2]), Qt.SolidPattern))
	painter.drawEllipse(20, 20, 60, 60)
	painter.end()
	return QIcon(pixmap)


def action_start() -> None:
	loop.get_timer().start()


def action_stop() -> None:
	loop.get_timer().stop()


def action_exit() -> None:
	print()
	sys.exit(wording.get('goodbye') + wording.get('exclamation_mark'))
