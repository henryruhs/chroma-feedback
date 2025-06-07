from typing import List, TypedDict

Args = TypedDict('Args',
{
	'buddy_host' : str,
	'buddy_slug' : List[str],
	'buddy_token' : str
})
