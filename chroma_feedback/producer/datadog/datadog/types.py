from typing import List, TypedDict

Args = TypedDict('Args',
{
	'datadog_host' : str,
	'datadog_slug' : List[str],
	'datadog_api_key' : str,
	'datadog_application_key' : str
})
