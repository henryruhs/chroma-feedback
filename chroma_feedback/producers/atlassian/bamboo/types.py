from typing import List, TypedDict

Args = TypedDict('Args',
{
	'atlassian_bamboo_host' : str,
	'atlassian_bamboo_slug' : List[str],
	'atlassian_bamboo_token' : str
})
