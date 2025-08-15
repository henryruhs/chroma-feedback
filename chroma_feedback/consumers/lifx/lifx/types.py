from typing import Any, List, TypeAlias, TypedDict

ImageConfig : TypeAlias = Any

Args = TypedDict('Args',
{
	'lifx_group_name' : List[str],
	'lifx_light_ip' : List[str]
})
