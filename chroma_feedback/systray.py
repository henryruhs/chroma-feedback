import sys
from typing import List
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush, QIcon, QPainter, QPixmap
from PyQt5.QtWidgets import QAction, QMenu, QSystemTrayIcon
from chroma_feedback import color, loop, wording
from chroma_feedback.typing import StatusType

SYSTRAY = None


def create(status : StatusType, report : List[str]) -> None:
	global SYSTRAY

	if not SYSTRAY:
		SYSTRAY = QSystemTrayIcon()
	update(status, report)


def update(status : StatusType, report : List[str]) -> None:
	global SYSTRAY

	SYSTRAY.setContextMenu(create_menu(report))
	SYSTRAY.setIcon(create_icon(status))
	SYSTRAY.hide()
	SYSTRAY.show()


def is_active() -> bool:
	global SYSTRAY

	return SYSTRAY is not None


def create_menu(report : List[str]) -> QMenu:
	menu = QMenu()
	timer = loop.get_timer()

	# process report

	for value in report:
		item_report = QAction(value)
		menu.addAction(item_report)
	if report:
		menu.addSeparator()

	# handle action

	item_exit = QAction(wording.get('start'))
	item_exit.triggered.connect(timer.start)
	item_exit = QAction(wording.get('stop'))
	item_exit.triggered.connect(timer.stop)
	item_exit = QAction(wording.get('exit'))
	item_exit.triggered.connect(destroy)
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


def destroy() -> None:
	print()
	sys.exit(wording.get('goodbye') + wording.get('exclamation_mark'))
