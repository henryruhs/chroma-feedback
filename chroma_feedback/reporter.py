from __future__ import print_function
from typing import List
from chroma_feedback import color, helper, metadata, wording
from chroma_feedback.typing import Consumer, Producer, Report, Status


def create_producer_report(producer_result : List[Producer]) -> List[Report]:
	report : List[Report] = []

	# process result

	for producer in producer_result:
		if producer['status'] == 'passed':
			report.append(
			{
				'symbol': color.format_passed(wording.get('tick')),
				'message': wording.get('has_status').format(producer['slug'], producer['producer'], 'passed'),
				'url': producer['url'],
				'status': producer['status']
			})
		if producer['status'] == 'started':
			report.append(
			{
				'symbol': color.format_started(wording.get('hourglass')),
				'message': wording.get('has_status').format(producer['slug'], producer['producer'], 'started'),
				'url': producer['url'],
				'status': producer['status']
			})
		if producer['status'] in ['errored', 'warned', 'failed']:
			report.append(
			{
				'symbol': color.format_by_status(wording.get('cross'), producer['status']),
				'message': wording.get('has_status').format(producer['slug'], producer['producer'], producer['status']),
				'url': producer['url'],
				'status': producer['status']
			})
	return report


def create_consumer_report(consumer_result : List[Consumer]) -> List[Report]:
	report : List[Report] = []

	# process result

	for consumer in consumer_result:
		if consumer['status'] == 'passed':
			report.append(
			{
				'symbol': color.format_passed(wording.get('tick')),
				'message': wording.get('set_status').format(consumer['name'], consumer['status']),
				'status': consumer['status']
			})
		if consumer['status'] == 'started':
			report.append(
			{
				'symbol': color.format_started(wording.get('hourglass')),
				'message': wording.get('set_status').format(consumer['name'], consumer['status']),
				'status': consumer['status']
			})
		if consumer['status'] in ['errored', 'warned', 'failed']:
			report.append(
			{
				'symbol': color.format_by_status(wording.get('cross'), consumer['status']),
				'message': wording.get('set_status').format(consumer['name'], consumer['status']),
				'status': consumer['status']
			})
	return report


def resolve_report_status(report : List[Report]) -> Status:
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


def print_report(report : List[Report]) -> None:
	for value in report:
		if helper.is_windows() is False:
			print(value['symbol'] + ' ' + value['message'])
		else:
			print(value['message'])
