import sys
import webbrowser
from typing import List

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QIcon, QPainter, QPixmap
from PyQt5.QtWidgets import QAction, QMenu, QSystemTrayIcon

from chroma_feedback import color, logger, loop, reporter, wording
from chroma_feedback.typing import ProducerReport, Status

SYSTRAY = None
MENU = None


def create(producer_report : List[ProducerReport]) -> None:
	global SYSTRAY, MENU

	if not SYSTRAY:
		SYSTRAY = QSystemTrayIcon()
	if not MENU:
		MENU = QMenu()
	update(producer_report)
	SYSTRAY.show()


def update(producer_report : List[ProducerReport]) -> None:
	global SYSTRAY, MENU

	status = reporter.resolve_report_status(producer_report)

	update_menu(producer_report)
	SYSTRAY.setContextMenu(MENU)
	SYSTRAY.setIcon(create_icon(status))


def is_created() -> bool:
	global SYSTRAY, MENU

	return SYSTRAY is not None and MENU is not None


def update_menu(producer_report : List[ProducerReport]) -> None:
	global MENU

	MENU.clear()

	# process report

	for report in producer_report:
		item_report = MENU.addAction(report['message'])
		item_report.setIcon(create_icon(report['status']))
		item_report.setIconVisibleInMenu(True)
		if 'url' in report and report['url']:
			item_report.triggered.connect(lambda __, url = report['url'] : webbrowser.open(url))
		else:
			item_report.setDisabled(True)
	if producer_report:
		MENU.addSeparator()

	# handle action

	item_start = MENU.addAction(wording.get('start'))
	item_stop = MENU.addAction(wording.get('stop'))
	item_exit = MENU.addAction(wording.get('exit'))
	item_start.setVisible(loop.get_timer().isActive() is False)
	item_stop.setVisible(loop.get_timer().isActive() is True)
	item_start.triggered.connect(lambda : action_start(item_start, item_stop))
	item_stop.triggered.connect(lambda : action_stop(item_start, item_stop))
	item_exit.triggered.connect(action_exit)


def create_icon(status : Status) -> QIcon:
	color_config = color.get_by_status(status)
	pixmap = QPixmap(100, 100)
	pixmap.fill(Qt.transparent)
	painter = QPainter(pixmap)
	painter.setBrush(QBrush(QColor(color_config['rgb'][0], color_config['rgb'][1], color_config['rgb'][2]), Qt.SolidPattern))
	painter.drawEllipse(20, 20, 60, 60)
	painter.end()
	return QIcon(pixmap)


def action_start(item_start : QAction, item_stop : QAction) -> None:
	item_start.setVisible(False)
	item_stop.setVisible(True)
	loop.get_timer().start()


def action_stop(item_start : QAction, item_stop : QAction) -> None:
	item_start.setVisible(True)
	item_stop.setVisible(False)
	loop.get_timer().stop()


def action_exit() -> None:
	logger.info(wording.get('goodbye') + wording.get('exclamation_mark'))
	sys.exit()
