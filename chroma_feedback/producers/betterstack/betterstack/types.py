from typing import List, TypedDict

Args = TypedDict('Args',
{
	'betterstack_host' : str,
	'betterstack_slug' : List[str],
	'betterstack_token' : str
})
