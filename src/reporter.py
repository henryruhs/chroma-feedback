from __future__ import print_function
import src.color as color
import src.wording as wording


def process_data(data):
	message = []
	status = 'passed'

	# process data

	for project in data:
		if project['active'] is True:
			if project['status'] == 'passed':
				message.append(color.green(wording.get('tick')) + ' ' + wording.get('build_passed').format(project['slug'], project['provider']))
			if project['status'] == 'process':
				message.append(color.yellow(wording.get('hourglass')) + ' ' + wording.get('build_process').format(project['slug'], project['provider']))
				if status != 'errored' and status != 'failed':
					status = 'process'
			if project['status'] == 'errored':
				message.append(wording.get('cross') + ' ' + wording.get('build_errored').format(project['slug'], project['provider']))
				if status != 'failed':
					status = 'errored'
			if project['status'] == 'failed':
				message.append(color.red(wording.get('cross')) + ' ' + wording.get('build_failed').format(project['slug'], project['provider']))
				status = 'failed'
	return\
	{
		'message': message,
		'status': status
	}


def print_result(result):
	if 'message' in result:
		for message in result['message']:
			print(message)
