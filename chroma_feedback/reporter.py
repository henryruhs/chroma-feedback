from __future__ import print_function
from typing import Any, List
from chroma_feedback import color, helper, metadata, wording
from chroma_feedback.typing import Consumer, ConsumerReport, Producer, ProducerReport, Status


def create_producer_report(producer_result : List[Producer]) -> List[ProducerReport]:
	report : List[ProducerReport] = []

	# process result

	for producer in producer_result:
		if producer['status'] == 'passed':
			report.append(
			{
				'name': producer['name'],
				'symbol': wording.get('tick'),
				'message': wording.get('has_status').format(producer['slug'], producer['name'], 'passed'),
				'url': producer['url'],
				'status': producer['status']
			})
		if producer['status'] == 'started':
			report.append(
			{
				'name': producer['name'],
				'symbol': wording.get('hourglass'),
				'message': wording.get('has_status').format(producer['slug'], producer['name'], 'started'),
				'url': producer['url'],
				'status': producer['status']
			})
		if producer['status'] in ['errored', 'warned', 'failed']:
			report.append(
			{
				'name': producer['name'],
				'symbol': wording.get('cross'),
				'message': wording.get('has_status').format(producer['slug'], producer['name'], producer['status']),
				'url': producer['url'],
				'status': producer['status']
			})
	return report


def create_consumer_report(consumer_result : List[Consumer]) -> List[ConsumerReport]:
	report : List[ConsumerReport] = []

	# process result

	for consumer in consumer_result:
		if consumer['status'] == 'passed':
			report.append(
			{
				'name': consumer['name'],
				'symbol': wording.get('tick'),
				'message': wording.get('set_status').format(consumer['description'], consumer['status']),
				'status': consumer['status']
			})
		if consumer['status'] == 'started':
			report.append(
			{
				'name': consumer['name'],
				'symbol': wording.get('hourglass'),
				'message': wording.get('set_status').format(consumer['description'], consumer['status']),
				'status': consumer['status']
			})
		if consumer['status'] in ['errored', 'warned', 'failed']:
			report.append(
			{
				'name': consumer['name'],
				'symbol': wording.get('cross'),
				'message': wording.get('set_status').format(consumer['description'], consumer['status']),
				'status': consumer['status']
			})
	return report


def resolve_report_status(report : List[Any]) -> Status:
	status: Status = 'passed'

	# process report

	for value in report:
		if value['status'] == 'started' and status not in ['errored', 'warned', 'failed']:
			status = 'started'
		if value['status'] == 'errored' and status not in ['warned', 'failed']:
			status = 'errored'
		if value['status'] == 'warned' and status != 'failed':
			status = 'warned'
		if value['status'] == 'failed':
			status = 'failed'
	return status


def print_header() -> None:
	print(metadata.get('name') + ' ' + metadata.get('version') + ' ' + wording.get('by') + ' ' + metadata.get('author'))


def print_report(report : List[Any]) -> None:
	for value in report:
		if helper.is_windows() is False:
			print(color.format_by_status(value['symbol'], value['status']) + ' ' + value['message'])
		else:
			print(value['message'])
