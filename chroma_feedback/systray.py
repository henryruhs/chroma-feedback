import sys
from typing import List
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush, QIcon, QPainter, QPixmap
from PyQt5.QtWidgets import QMenu, QSystemTrayIcon
from chroma_feedback import color, loop, wording
from chroma_feedback.typing import StatusType, ReportModel

SYSTRAY = None


def create(status : StatusType, report : List[ReportModel]) -> None:
	global SYSTRAY

	if not SYSTRAY:
		SYSTRAY = QSystemTrayIcon()
	update(status, report)
	SYSTRAY.show()


def update(status : StatusType, report : List[ReportModel]) -> None:
	global SYSTRAY

	SYSTRAY.setContextMenu(create_menu(report))
	SYSTRAY.setIcon(create_icon(status))
	refresh()


def is_created() -> bool:
	global SYSTRAY

	return SYSTRAY is not None


def create_menu(report : List[ReportModel]) -> QMenu:
	menu = QMenu()
	timer = loop.get_timer()

	# process report

	for value in report:
		item_report = menu.addAction(value['message'])
		item_report.setIcon(create_icon(value['status']))
		item_report.setIconVisibleInMenu(True)
	if report:
		menu.addSeparator()

	# handle action

	item_start = menu.addAction(wording.get('start'))
	item_start.triggered.connect(timer.start)
	item_stop = menu.addAction(wording.get('stop'))
	item_stop.triggered.connect(timer.stop)
	item_exit = menu.addAction(wording.get('exit'))
	item_exit.triggered.connect(destroy)
	menu.addAction(item_start)
	menu.addAction(item_stop)
	menu.addAction(item_exit)
	return menu


def create_icon(status : StatusType) -> QIcon:
	color_config = color.get_by_status(status)
	pixmap = QPixmap(100, 100)
	pixmap.fill(Qt.transparent)
	painter = QPainter(pixmap)
	painter.setBrush(QBrush(QColor(color_config['rgb'][0], color_config['rgb'][1], color_config['rgb'][2]), Qt.SolidPattern))
	painter.drawEllipse(20, 20, 60, 60)
	painter.end()
	return QIcon(pixmap)


def refresh() -> None:
	global SYSTRAY

	SYSTRAY.hide()
	SYSTRAY.show()


def destroy() -> None:
	print()
	sys.exit(wording.get('goodbye') + wording.get('exclamation_mark'))
