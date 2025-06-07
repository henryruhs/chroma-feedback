from typing import List, TypedDict

Args = TypedDict('Args',
{
	'travis_host' : str,
	'travis_slug' : List[str],
	'travis_token' : str
})
