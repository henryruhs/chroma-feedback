from typing import List, TypedDict

AzureArgs = TypedDict('AzureArgs',
{
	'microsoft_azure_host' : str,
	'microsoft_azure_slug' : List[str],
	'microsoft_azure_token' : str
})

GitHubArgs = TypedDict('GitHubArgs',
{
	'microsoft_github_host' : str,
	'microsoft_github_slug' : List[str],
	'microsoft_github_token' : str
})
