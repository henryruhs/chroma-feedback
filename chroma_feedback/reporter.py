import os
from typing import Any, List

from chroma_feedback import color, helper, logger, metadata, wording
from chroma_feedback.types import Consumer, ConsumerReport, Producer, ProducerReport, Status


def create_producer_report(producer_result : List[Producer]) -> List[ProducerReport]:
	report : List[ProducerReport] = []

	for result in producer_result:
		if result.get('status') == 'passed':
			report.append(
			{
				'name': result.get('name'),
				'symbol': wording.get('tick'),
				'message': wording.get('has_status').format(result.get('slug'), result.get('name'), 'passed'),
				'url': result.get('url'),
				'status': result.get('status')
			})
		if result.get('status') == 'started':
			report.append(
			{
				'name': result.get('name'),
				'symbol': wording.get('hourglass'),
				'message': wording.get('has_status').format(result.get('slug'), result.get('name'), 'started'),
				'url': result.get('url'),
				'status': result.get('status')
			})
		if result.get('status') in [ 'errored', 'warned', 'failed' ]:
			report.append(
			{
				'name': result.get('name'),
				'symbol': wording.get('cross'),
				'message': wording.get('has_status').format(result.get('slug'), result.get('name'), result.get('status')),
				'url': result.get('url'),
				'status': result.get('status')
			})
	return report


def create_consumer_report(consumer_result : List[Consumer]) -> List[ConsumerReport]:
	report : List[ConsumerReport] = []

	for result in consumer_result:
		if result.get('status') == 'passed':
			report.append(
			{
				'name': result.get('name'),
				'symbol': wording.get('tick'),
				'message': wording.get('set_status').format(result.get('description'), result.get('status')),
				'status': result.get('status')
			})
		if result.get('status') == 'started':
			report.append(
			{
				'name': result.get('name'),
				'symbol': wording.get('hourglass'),
				'message': wording.get('set_status').format(result.get('description'), result.get('status')),
				'status': result.get('status')
			})
		if result.get('status') in [ 'errored', 'warned', 'failed' ]:
			report.append(
			{
				'name': result.get('name'),
				'symbol': wording.get('cross'),
				'message': wording.get('set_status').format(result.get('description'), result.get('status')),
				'status': result.get('status')
			})
	return report


def resolve_report_status(producer_report : List[ProducerReport]) -> Status:
	status : Status = 'passed'

	for report in producer_report:
		if report.get('status') == 'started' and status not in [ 'errored', 'warned', 'failed' ]:
			status = 'started'
		if report.get('status') == 'errored' and status not in [ 'warned', 'failed' ]:
			status = 'errored'
		if report.get('status') == 'warned' and status != 'failed':
			status = 'warned'
		if report.get('status') == 'failed':
			status = 'failed'
	return status


def print_header() -> None:
	logger.info(metadata.get('name') + ' ' + metadata.get('version') + ' ' + wording.get('by') + ' ' + metadata.get('author'))
	logger.info(os.linesep)


def print_report(report : List[Any]) -> None:
	for value in report:
		if not helper.is_windows():
			logger.info(color.format_by_status(value.get('symbol'), value.get('status')) + ' ' + value.get('message'))
		else:
			logger.info(value.get('message'))
	logger.info(os.linesep)
