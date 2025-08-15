from typing import List, TypedDict

Args = TypedDict('Args',
{
	'appveyor_host' : str,
	'appveyor_slug' : List[str],
	'appveyor_token' : str
})
