from typing import List, TypedDict

Args = TypedDict('Args',
{
	'netlify_host' : str,
	'netlify_slug' : List[str],
	'netlify_token' : str
})
