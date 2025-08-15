from typing import List, TypedDict

Args = TypedDict('Args',
{
	'uptimerobot_host' : str,
	'uptimerobot_slug' : List[str],
	'uptimerobot_token' : str
})
