from src import color, metadata, wording


def create_provider_report(provider_result):
	message = []

	# process data

	for project in provider_result:
		if project['active'] is True:
			if project['status'] == 'passed':
				message.append(color.green(wording.get('tick')) + ' ' + wording.get('build_passed').format(project['slug'], project['provider']))
			if project['status'] == 'process':
				message.append(color.yellow(wording.get('hourglass')) + ' ' + wording.get('build_process').format(project['slug'], project['provider']))
			if project['status'] == 'errored':
				message.append(wording.get('cross') + ' ' + wording.get('build_errored').format(project['slug'], project['provider']))
			if project['status'] == 'failed':
				message.append(color.red(wording.get('cross')) + ' ' + wording.get('build_failed').format(project['slug'], project['provider']))
	return\
	{
		'message': message
	}


def create_consumer_report(consumer_result):
	return consumer_result


def print_header():
	print(metadata.get('name') + ' ' + metadata.get('version') + ' ' + wording.get('by') + ' ' + metadata.get('author'))


def print_provider_report(provider_result):
	if 'message' in provider_result:
		for message in provider_result['message']:
			print(message)


def print_consumer_report(consumer_result):
	print(consumer_result)
