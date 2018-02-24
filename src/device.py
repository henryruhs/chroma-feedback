from src import wording


def process(data, status):
	message = []

	# process data

	for device in data:
		if status == 'passed' and static(device.fx, [0, 255, 0]):
			message.append(wording.get('setting_passed').format(device.name) + wording.get('point'))
		if status == 'process' and static(device.fx, [255, 255, 0]):
			message.append(wording.get('setting_process').format(device.name) + wording.get('point'))
		if status == 'errored' and pulsate(device.fx, [255, 255, 255]):
			message.append(wording.get('setting_errored').format(device.name) + wording.get('point'))
		if status == 'failed' and pulsate(device.fx, [255, 0, 0]):
			message.append(wording.get('setting_failed').format(device.name) + wording.get('point'))
	return\
	{
		'message': message,
		'status': status
	}


def static(fx, rgb):
	if fx.has('logo') and fx.has('scroll'):
		return fx.misc.logo.static(rgb[0], rgb[1], rgb[2]) and fx.misc.scroll_wheel.static(rgb[0], rgb[1], rgb[2])
	return fx.static(rgb[0], rgb[1], rgb[2])


def pulsate(fx, rgb):
	if fx.has('logo') and fx.has('scroll'):
		return fx.misc.logo.pulsate(rgb[0], rgb[1], rgb[2]) and fx.misc.scroll_wheel.pulsate(rgb[0], rgb[1], rgb[2])
	return fx.breath_single(rgb[0], rgb[1], rgb[2])
