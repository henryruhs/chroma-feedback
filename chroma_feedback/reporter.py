from typing import Any, List

from chroma_feedback import color, helper, logger, metadata, wording
from chroma_feedback.typing import Consumer, ConsumerReport, Producer, ProducerReport, Status


def create_producer_report(producer_result : List[Producer]) -> List[ProducerReport]:
	report : List[ProducerReport] = []

	for result in producer_result:
		if result['status'] == 'passed':
			report.append(
			{
				'name': result['name'],
				'symbol': wording.get('tick'),
				'message': wording.get('has_status').format(result['slug'], result['name'], 'passed'),
				'url': result['url'],
				'status': result['status']
			})
		if result['status'] == 'started':
			report.append(
			{
				'name': result['name'],
				'symbol': wording.get('hourglass'),
				'message': wording.get('has_status').format(result['slug'], result['name'], 'started'),
				'url': result['url'],
				'status': result['status']
			})
		if result['status'] in ['errored', 'warned', 'failed']:
			report.append(
			{
				'name': result['name'],
				'symbol': wording.get('cross'),
				'message': wording.get('has_status').format(result['slug'], result['name'], result['status']),
				'url': result['url'],
				'status': result['status']
			})
	return report


def create_consumer_report(consumer_result : List[Consumer]) -> List[ConsumerReport]:
	report : List[ConsumerReport] = []

	for result in consumer_result:
		if result['status'] == 'passed':
			report.append(
			{
				'name': result['name'],
				'symbol': wording.get('tick'),
				'message': wording.get('set_status').format(result['description'], result['status']),
				'status': result['status']
			})
		if result['status'] == 'started':
			report.append(
			{
				'name': result['name'],
				'symbol': wording.get('hourglass'),
				'message': wording.get('set_status').format(result['description'], result['status']),
				'status': result['status']
			})
		if result['status'] in ['errored', 'warned', 'failed']:
			report.append(
			{
				'name': result['name'],
				'symbol': wording.get('cross'),
				'message': wording.get('set_status').format(result['description'], result['status']),
				'status': result['status']
			})
	return report


def resolve_report_status(producer_report : List[ProducerReport]) -> Status:
	status : Status = 'passed'

	for report in producer_report:
		if report['status'] == 'started' and status not in ['errored', 'warned', 'failed']:
			status = 'started'
		if report['status'] == 'errored' and status not in ['warned', 'failed']:
			status = 'errored'
		if report['status'] == 'warned' and status != 'failed':
			status = 'warned'
		if report['status'] == 'failed':
			status = 'failed'
	return status


def print_header() -> None:
	logger.info(metadata.get('name') + ' ' + metadata.get('version') + ' ' + wording.get('by') + ' ' + metadata.get('author'))
	logger.info()


def print_report(report : List[Any]) -> None:
	for value in report:
		if not helper.is_windows():
			logger.info(color.format_by_status(value['symbol'], value['status']) + ' ' + value['message'])
		else:
			logger.info(value['message'])
	logger.info()
