from typing import List, TypedDict

Args = TypedDict('Args',
{
	'vercel_host' : str,
	'vercel_slug' : List[str],
	'vercel_token' : str
})
