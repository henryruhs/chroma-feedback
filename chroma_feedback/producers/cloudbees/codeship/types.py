from typing import List, TypedDict

Args = TypedDict('Args',
{
	'cloudbees_codeship_host' : str,
	'cloudbees_codeship_slug' : List[str],
	'cloudbees_codeship_username' : str,
	'cloudbees_codeship_password': str
})
