from typing import List, TypedDict

Args = TypedDict('Args',
{
	'atlassian_bitbucket_host' : str,
	'atlassian_bitbucket_slug' : List[str],
	'atlassian_bitbucket_username' : str,
	'atlassian_bitbucket_password' : str
})
