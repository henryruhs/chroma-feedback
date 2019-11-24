from __future__ import print_function
from typing import Any, Dict, List
from chroma_feedback import color, metadata, wording


def create_provider_report(provider_result : List[Dict[str, Any]]) -> List[str]:
	report = []

	# process result

	for provider in provider_result:
		if provider['active'] is True:
			if provider['status'] == 'passed':
				report.append(color.format_green(wording.get('tick')) + ' ' + wording.get('build_passed').format(provider['slug'], provider['provider']))
			if provider['status'] == 'process':
				report.append(color.format_yellow(wording.get('hourglass')) + ' ' + wording.get('build_process').format(provider['slug'], provider['provider']))
			if provider['status'] == 'errored':
				report.append(wording.get('cross') + ' ' + wording.get('build_errored').format(provider['slug'], provider['provider']))
			if provider['status'] == 'failed':
				report.append(color.format_red(wording.get('cross')) + ' ' + wording.get('build_failed').format(provider['slug'], provider['provider']))
	return report


def create_consumer_report(consumer_result : List[Dict[str, Any]]) -> List[str]:
	report = []

	# process result

	for consumer in consumer_result:
		if consumer['active'] is True:
			if consumer['status'] == 'passed':
				report.append(color.format_green(wording.get('tick')) + ' ' + wording.get('setting_passed').format(consumer['name']) + wording.get('point'))
			if consumer['status'] == 'process':
				report.append(color.format_yellow(wording.get('hourglass')) + ' ' + wording.get('setting_process').format(consumer['name']) + wording.get('point'))
			if consumer['status'] == 'errored':
				report.append(wording.get('cross') + ' ' + wording.get('setting_errored').format(consumer['name']) + wording.get('point'))
			if consumer['status'] == 'failed':
				report.append(color.format_red(wording.get('cross')) + ' ' + wording.get('setting_failed').format(consumer['name']) + wording.get('point'))
	return report


def print_header() -> None:
	print(metadata.get('name') + ' ' + metadata.get('version') + ' ' + wording.get('by') + ' ' + metadata.get('author'))


def print_report(report : List[str]) -> None:
	for message in report:
		print(message)
