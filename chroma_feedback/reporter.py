from __future__ import print_function
from typing import Any, Dict, List
from chroma_feedback import color, metadata, wording


def create_producer_report(producer_result : List[Dict[str, Any]]) -> List[str]:
	report = []

	# process result

	for producer in producer_result:
		if producer['active'] is True:
			if producer['status'] == 'passed':
				report.append(color.format_passed(wording.get('tick')) + ' ' + wording.get('build_passed').format(producer['slug'], producer['producer']))
			if producer['status'] == 'started':
				report.append(color.format_started(wording.get('hourglass')) + ' ' + wording.get('build_started').format(producer['slug'], producer['producer']))
			if producer['status'] == 'errored':
				report.append(wording.get('cross') + ' ' + wording.get('build_errored').format(producer['slug'], producer['producer']))
			if producer['status'] == 'failed':
				report.append(color.format_failed(wording.get('cross')) + ' ' + wording.get('build_failed').format(producer['slug'], producer['producer']))
	return report


def create_consumer_report(consumer_result : List[Dict[str, Any]]) -> List[str]:
	report = []

	# process result

	for consumer in consumer_result:
		if consumer['active'] is True:
			if consumer['status'] == 'passed':
				report.append(color.format_passed(wording.get('tick')) + ' ' + wording.get('setting_passed').format(consumer['name']) + wording.get('point'))
			if consumer['status'] == 'started':
				report.append(color.format_started(wording.get('hourglass')) + ' ' + wording.get('setting_started').format(consumer['name']) + wording.get('point'))
			if consumer['status'] == 'errored':
				report.append(wording.get('cross') + ' ' + wording.get('setting_errored').format(consumer['name']) + wording.get('point'))
			if consumer['status'] == 'failed':
				report.append(color.format_failed(wording.get('cross')) + ' ' + wording.get('setting_failed').format(consumer['name']) + wording.get('point'))
	return report


def create_systray_report(producer_result : List[Dict[str, Any]]) -> List[str]:
	report = []

	# process result

	for producer in producer_result:
		if producer['active'] is True:
			if producer['status'] == 'passed':
				report.append(wording.get('build_passed').format(producer['slug'], producer['producer']))
			if producer['status'] == 'started':
				report.append(wording.get('build_started').format(producer['slug'], producer['producer']))
			if producer['status'] == 'errored':
				report.append(wording.get('build_errored').format(producer['slug'], producer['producer']))
			if producer['status'] == 'failed':
				report.append(wording.get('build_failed').format(producer['slug'], producer['producer']))
	return report


def print_header() -> None:
	print(metadata.get('name') + ' ' + metadata.get('version') + ' ' + wording.get('by') + ' ' + metadata.get('author'))


def print_report(report : List[str]) -> None:
	for message in report:
		print(message)
