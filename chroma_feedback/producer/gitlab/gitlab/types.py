from typing import List, TypedDict

Args = TypedDict('Args',
{
	'gitlab_host' : str,
	'gitlab_slug' : List[str],
	'gitlab_token' : str
})
