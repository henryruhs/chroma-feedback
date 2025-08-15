from typing import List, TypedDict

Args = TypedDict('Args',
{
	'microsoft_azure_host' : str,
	'microsoft_azure_slug' : List[str],
	'microsoft_azure_token' : str
})
