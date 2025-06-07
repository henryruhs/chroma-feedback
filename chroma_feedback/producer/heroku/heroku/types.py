from typing import List, TypedDict

Args = TypedDict('Args',
{
	'heroku_host' : str,
	'heroku_slug' : List[str],
	'heroku_token' : str
})
