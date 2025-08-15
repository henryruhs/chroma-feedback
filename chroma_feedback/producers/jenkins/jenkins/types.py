from typing import List, TypedDict

Args = TypedDict('Args',
{
	'jenkins_host' : str,
	'jenkins_slug' : List[str],
	'jenkins_username': str,
	'jenkins_token' : str
})
