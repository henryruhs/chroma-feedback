import base64
import requests
from chroma_feedback import helper
from .normalize import normalize_data

args = None


def init(program):
	global args

	if not args:
		program.add_argument('--teamcity-host', default = 'https://teamcity.jetbrains.com')
		program.add_argument('--teamcity-slug', action = 'append')
		program.add_argument('--teamcity-username', required = True)
		program.add_argument('--teamcity-password', required = True)
	args = program.parse_known_args()[0]


def run():
	result = []

	if args.teamcity_slug:
		for slug in args.teamcity_slug:
			result.extend(fetch(args.teamcity_host, slug, args.teamcity_username, args.teamcity_password))
	else:
		result.extend(fetch(args.teamcity_host, None, args.teamcity_username, args.teamcity_password))
	return result


def fetch(host, slug, username, password):
	response = None

	if host and username and password:
		username_password = username + ':' + password
		headers =\
		{
			'Accept': 'application/json',
			'Authorization': 'Basic ' + base64.b64encode(username_password.encode('utf-8')).decode('ascii')
		}
		if slug:
			response = requests.get(host + '/app/rest/buildTypes?locator=affectedProject:(id:' + slug + ')&fields=buildType(builds($locator(running:any),build(id,running,status,buildType(id,projectName))))', headers = headers)
		else:
			response = requests.get(host + '/app/rest/buildTypes/?fields=buildType(builds($locator(user:current,running:any),build(id,running,status,buildType(id,projectName))))', headers = headers)

	# process response

	if response and response.status_code == 200:
		data = helper.parse_json(response)

		if 'buildType' in data:
			result = []

			for project in data['buildType']:
				if project['builds']['build']:
					result.extend(normalize_data(project['builds']['build'][0]))
			return result
	return []
