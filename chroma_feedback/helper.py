from typing import Any, Dict, List
import sys


def get_provider_status(provider_result : List[Dict[str, Any]]) -> str:
	status = 'passed'

	# process provider

	for project in provider_result:
		if project['active'] is True:
			if project['status'] == 'process':
				if status not in ['errored', 'failed']:
					status = 'process'
			if project['status'] == 'errored':
				if status != 'failed':
					status = 'errored'
			if project['status'] == 'failed':
				status = 'failed'
	return status


def parse_json(response):
	try:
		return response.json()
	except ValueError:
		return []


def has_argument(argument):
	return any(argument in argv for argv in sys.argv)
