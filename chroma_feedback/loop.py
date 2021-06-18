import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication

APPLIACTION = None
TIMER = None


def get_application() -> QApplication:
	global APPLIACTION

	if APPLIACTION is None:
		APPLIACTION = QApplication(sys.argv)
	return APPLIACTION


def get_timer() -> QTimer:
	global TIMER

	if TIMER is None:
		TIMER = QTimer()
	return TIMER


def is_created() -> bool:
	global APPLIACTION, TIMER

	return APPLIACTION is not None and TIMER is not None
