from typing import Dict, List, Literal, Optional, TypedDict

Status = Literal\
[
	'skipped',
	'passed',
	'started',
	'errored',
	'warned',
	'failed'
]
ProducerName = Literal\
[
	'appveyor',
	'azure',
	'bamboo',
	'bitbucket',
	'buddy',
	'circle',
	'codeship',
	'custom',
	'datadog',
	'github',
	'gitlab',
	'heroku',
	'jenkins',
	'netlify',
	'teamcity',
	'travis',
	'vercel',
	'wercker'
]
ConsumerName = Literal\
[
	'agile_innovative_blinkstick',
	'elgato_streamdeck',
	'embrava_blynclight',
	'kuando_busylight',
	'lifx_light',
	'luxafor_flag',
	'magic_hue',
	'nanoleaf_light',
	'philips_hue',
	'razer_chroma',
	'thingm_blink1',
	'wiz_light',
	'xiaomi_yeelight'
]
ConsumerType = Literal\
[
	'light',
	'device',
	'group'
]
LogLevel = Literal\
[
	'error',
	'warn',
	'info',
	'debug'
]
Headers = Dict[str, str]

class Producer(TypedDict):
	name: ProducerName
	slug: str
	url: Optional[str]
	status: Status


class Consumer(TypedDict):
	name: ConsumerName
	type: ConsumerType
	description: str
	status: Status


class ProducerReport(TypedDict):
	name: ProducerName
	symbol: str
	message : str
	url : Optional[str]
	status : Status


class ConsumerReport(TypedDict):
	name: ConsumerName
	symbol: str
	message : str
	status : Status


class Color(TypedDict):
	name: str
	rgb: List[int]
	hue: int
	saturation: List[int]
	brightness: List[int]
	kelvin: int
