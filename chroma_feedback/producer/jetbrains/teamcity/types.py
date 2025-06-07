from typing import List, TypedDict

Args = TypedDict('Args',
{
	'jetbrains_teamcity_host' : str,
	'jetbrains_teamcity_slug' : List[str],
	'jetbrains_teamcity_token' : str
})
