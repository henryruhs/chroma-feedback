from typing import Any, Dict, List, Literal, Optional, TypeAlias, TypedDict

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
	'betterstack',
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
	'uptimerobot',
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
Data : TypeAlias = Any
Json : TypeAlias = Any
Headers : TypeAlias = Dict[str, str]

Producer = TypedDict('Producer',
{
	'name' : ProducerName,
	'slug' : str,
	'url' : Optional[str],
	'status' : Status
})

Consumer = TypedDict('Consumer',
{
	'name' : ConsumerName,
	'type' : ConsumerType,
	'description' : str,
	'status' : Status
})

ProducerReport = TypedDict('ProducerReport',
{
	'name' : ProducerName,
	'symbol' : str,
	'message' : str,
	'url' : Optional[str],
	'status' : Status
})

ConsumerReport = TypedDict('ConsumerReport',
{
	'name' : ConsumerName,
	'symbol' : str,
	'message' : str,
	'status' : Status
})

ColorConfig = TypedDict('ColorConfig',
{
	'rgb' : List[int],
	'hue' : int,
	'saturation' : List[int],
	'brightness' : List[int],
	'kelvin' : int
})

Api : TypeAlias = Any
Light : TypeAlias = Any
Device : TypeAlias = Any
Group : TypeAlias = Any
