from typing import TypedDict, List

GitHubArgs = TypedDict('GitHubArgs',
{
	'microsoft_github_host' : str,
	'microsoft_github_slug' : List[str],
	'microsoft_github_token' : str
})
