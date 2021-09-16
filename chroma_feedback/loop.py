import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication

APPLICATION = None
TIMER = None


def get_application() -> QApplication:
	global APPLICATION

	if APPLICATION is None:
		APPLICATION = QApplication(sys.argv)
	return APPLICATION


def get_timer() -> QTimer:
	global TIMER

	if TIMER is None:
		TIMER = QTimer()
	return TIMER


def is_created() -> bool:
	global APPLICATION, TIMER

	return APPLICATION is not None and TIMER is not None
