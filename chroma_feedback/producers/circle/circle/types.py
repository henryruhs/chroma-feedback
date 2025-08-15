from typing import List, TypedDict

Args = TypedDict('Args',
{
	'circle_host' : str,
	'circle_organization' : str,
	'circle_slug' : List[str],
	'circle_token' : str
})
