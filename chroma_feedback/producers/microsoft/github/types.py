from typing import List, TypedDict

Args = TypedDict('Args',
{
	'microsoft_github_host' : str,
	'microsoft_github_slug' : List[str],
	'microsoft_github_token' : str
})
