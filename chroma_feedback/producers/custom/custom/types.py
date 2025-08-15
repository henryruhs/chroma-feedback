from typing import List, TypedDict

Args = TypedDict('Args',
{
	'custom_host' : str,
	'custom_slug' : List[str],
	'custom_token' : str
})
