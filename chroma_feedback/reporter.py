from __future__ import print_function
from typing import List
from chroma_feedback import color, helper, metadata, wording
from chroma_feedback.typing import Consumer, Producer, Report


def create_producer_report(producer_result : List[Producer]) -> List[Report]:
	report : List[Report] = []

	# process result

	for producer in producer_result:
		if producer['active'] is True:
			if producer['status'] == 'passed':
				report.append(
				{
					'status': 'passed',
					'message': wording.get('has_status').format(producer['slug'], producer['producer'], 'passed'),
					'symbol': color.format_passed(wording.get('tick'))
				})
			if producer['status'] == 'started':
				report.append(
				{
					'status': 'started',
					'message': wording.get('has_status').format(producer['slug'], producer['producer'], 'started'),
					'symbol': color.format_started(wording.get('hourglass'))
				})
			if producer['status'] == 'errored':
				report.append(
				{
					'status': 'errored',
					'message': wording.get('has_status').format(producer['slug'], producer['producer'], 'errored'),
					'symbol': color.format_errored(wording.get('cross'))
				})
			if producer['status'] == 'warned':
				report.append(
				{
					'status': 'warned',
					'message': wording.get('has_status').format(producer['slug'], producer['producer'], 'warned'),
					'symbol': color.format_warned(wording.get('cross'))
				})
			if producer['status'] == 'failed':
				report.append(
				{
					'status': 'failed',
					'message': wording.get('has_status').format(producer['slug'], producer['producer'], 'failed'),
					'symbol': color.format_failed(wording.get('cross'))
				})
	return report


def create_consumer_report(consumer_result : List[Consumer]) -> List[Report]:
	report : List[Report] = []

	# process result

	for consumer in consumer_result:
		if consumer['active'] is True:
			if consumer['status'] == 'passed':
				report.append(
				{
					'status': 'passed',
					'message': wording.get('set_status').format(consumer['name'], 'passed'),
					'symbol': color.format_passed(wording.get('tick'))
				})
			if consumer['status'] == 'started':
				report.append(
				{
					'status': 'started',
					'message': wording.get('set_status').format(consumer['name'], 'started'),
					'symbol': color.format_started(wording.get('hourglass'))
				})
			if consumer['status'] == 'errored':
				report.append(
				{
					'status': 'errored',
					'message': wording.get('set_status').format(consumer['name'], 'errored'),
					'symbol': color.format_errored(wording.get('cross'))
				})
			if consumer['status'] == 'warned':
				report.append(
				{
					'status': 'warned',
					'message': wording.get('set_status').format(consumer['name'], 'warned'),
					'symbol': color.format_warned(wording.get('cross'))
				})
			if consumer['status'] == 'failed':
				report.append(
				{
					'status': 'failed',
					'message': wording.get('set_status').format(consumer['name'], 'failed'),
					'symbol': color.format_failed(wording.get('cross'))
				})
	return report


def print_header() -> None:
	print(metadata.get('name') + ' ' + metadata.get('version') + ' ' + wording.get('by') + ' ' + metadata.get('author'))


def print_report(report : List[Report]) -> None:
	for value in report:
		if helper.is_windows() is False:
			print(value['symbol'] + ' ' + value['message'])
		else:
			print(value['message'])
