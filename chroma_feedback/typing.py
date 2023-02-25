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
	'atlassian.bamboo',
	'atlassian.bitbucket',
	'buddy',
	'circle',
	'cloudbees.codeship',
	'custom',
	'datadog',
	'gitlab',
	'heroku',
	'jenkins',
	'jetbrains.teamcity',
	'microsoft.azure',
	'microsoft.github',
	'netlify',
	'travis',
	'vercel'
]
ConsumerName = Literal\
[
	'agile_innovative.blinkstick',
	'compulab.fit_statusb',
	'elgato.streamdeck',
	'embrava.blynclight',
	'embrava.blynclight_mini',
	'embrava.blynclight_plus',
	'gigabyte.rgb_fusion2',
	'kuando.busylight_alpha',
	'kuando.busylight_omega',
	'lifx',
	'luxafor.flag',
	'luxafor.mute',
	'luxafor.orb',
	'magic.hue',
	'muteme',
	'muteme.muteme_mini',
	'mutesync',
	'nanoleaf',
	'philips.hue',
	'plantronics.status_indicator',
	'razer.chroma',
	'signify.wiz',
	'thingm.blink1',
	'xiaomi.yeelight'
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
	rgb: List[int]
	hue: int
	saturation: List[int]
	brightness: List[int]
	kelvin: int
