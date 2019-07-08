from __future__ import print_function
from src import color, metadata, wording


def create_provider_report(provider_result):
	report = []

	# process result

	for project in provider_result:
		if project['active'] is True:
			if project['status'] == 'passed':
				report.append(color.green(wording.get('tick')) + ' ' + wording.get('build_passed').format(project['slug'], project['provider']))
			if project['status'] == 'process':
				report.append(color.yellow(wording.get('hourglass')) + ' ' + wording.get('build_process').format(project['slug'], project['provider']))
			if project['status'] == 'errored':
				report.append(wording.get('cross') + ' ' + wording.get('build_errored').format(project['slug'], project['provider']))
			if project['status'] == 'failed':
				report.append(color.red(wording.get('cross')) + ' ' + wording.get('build_failed').format(project['slug'], project['provider']))
	return report


def create_consumer_report(consumer_result):
	report = []

	# process result

	for device in consumer_result:
		if device['active'] is True:
			if device['status'] == 'passed':
				report.append(color.green(wording.get('tick')) + ' ' + wording.get('setting_passed').format(device['name']) + wording.get('point'))
			if device['status'] == 'process':
				report.append(color.yellow(wording.get('hourglass')) + ' ' + wording.get('setting_process').format(device['name']) + wording.get('point'))
			if device['status'] == 'errored':
				report.append(wording.get('cross') + ' ' + wording.get('setting_errored').format(device['name']) + wording.get('point'))
			if device['status'] == 'failed':
				report.append(color.red(wording.get('cross')) + ' ' + wording.get('setting_failed').format(device['name']) + wording.get('point'))
	return report


def print_header():
	print(metadata.get('name') + ' ' + metadata.get('version') + ' ' + wording.get('by') + ' ' + metadata.get('author'))


def print_report(report):
	for message in report:
		print(message)
