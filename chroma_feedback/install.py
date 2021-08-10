import os
from setuptools.command.install import install
from chroma_feedback import helper


class InstallCommand(install):
	@staticmethod
	def write_rule() -> None:
		with open('/etc/udev/rules.d/99-chroma-feedback.rules', 'w+') as file:
			file.write('SUBSYSTEM=="usb", MODE="0666"')
			file.close()


	@staticmethod
	def load_rule() -> None:
		os.system('udevadm control --reload')
		os.system('udevadm trigger')


	def run(self) -> None:
		install.run(self)

		if helper.is_linux() is True and helper.is_root() is True:
			self.write_rule()
			self.load_rule()
