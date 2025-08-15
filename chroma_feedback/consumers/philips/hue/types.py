from typing import List, TypedDict

Args = TypedDict('Args',
{
	'philips_hue_bridge_ip' : str,
	'philips_hue_group_name' : List[str],
	'philips_hue_light_id' : List[str]
})
