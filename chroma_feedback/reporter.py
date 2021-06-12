from __future__ import print_function
from typing import List
from chroma_feedback import color, metadata, wording
from chroma_feedback.typing import ConsumerModel, ProducerModel, ReportModel


def create_producer_report(producer_result : List[ProducerModel]) -> List[ReportModel]:
	report = []

	# process result

	for producer in producer_result:
		if producer['active'] is True:
			if producer['status'] == 'passed':
				report.append(
				{
					'status': 'passed',
					'message': wording.get('build_passed').format(producer['slug'], producer['producer']),
					'symbol': color.format_passed(wording.get('tick'))
				})
			if producer['status'] == 'started':
				report.append(
				{
					'status': 'started',
					'message': wording.get('build_started').format(producer['slug'], producer['producer']),
					'symbol': color.format_started(wording.get('hourglass'))
				})
			if producer['status'] == 'errored':
				report.append(
				{
					'status': 'errored',
					'message': wording.get('build_errored').format(producer['slug'], producer['producer']),
					'symbol': wording.get('cross')
				})
			if producer['status'] == 'failed':
				report.append(
				{
					'status': 'failed',
					'message': wording.get('build_errored').format(producer['slug'], producer['producer']),
					'symbol': color.format_failed(wording.get('cross'))
				})
	return report


def create_consumer_report(consumer_result : List[ConsumerModel]) -> List[ReportModel]:
	report = []

	# process result

	for consumer in consumer_result:
		if consumer['active'] is True:
			if consumer['status'] == 'passed':
				report.append(
				{
					'status': 'passed',
					'message': wording.get('setting_passed').format(consumer['name']) + wording.get('point'),
					'symbol': color.format_passed(wording.get('tick'))
				})
			if consumer['status'] == 'started':
				report.append(
				{
					'status': 'started',
					'message': wording.get('setting_started').format(consumer['name']) + wording.get('point'),
					'symbol': color.format_started(wording.get('hourglass'))
				})
			if consumer['status'] == 'errored':
				report.append(
				{
					'status': 'errored',
					'message': wording.get('setting_errored').format(consumer['name']) + wording.get('point'),
					'symbol': wording.get('cross')
				})
			if consumer['status'] == 'failed':
				report.append(
				{
					'status': 'failed',
					'message': wording.get('setting_failed').format(consumer['name']) + wording.get('point'),
					'symbol': color.format_failed(wording.get('cross'))
				})
	return report


def print_header() -> None:
	print(metadata.get('name') + ' ' + metadata.get('version') + ' ' + wording.get('by') + ' ' + metadata.get('author'))


def print_report(report : List[ReportModel]) -> None:
	for value in report:
		print(value['symbol'] + ' ' + value['message'])
