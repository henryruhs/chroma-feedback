from typing import Literal, TypedDict, Optional, List

Status = Literal['skipped', 'passed', 'started', 'errored', 'warned', 'failed']
ConsumerType = Literal['light', 'device', 'group']


class Producer(TypedDict):
	producer: str
	slug: str
	url: Optional[str]
	status: Status


class Consumer(TypedDict):
	consumer: str
	type: ConsumerType
	name: str
	status: Status


class Report(TypedDict):
	symbol: str
	message : str
	url : Optional[str]
	status : Status


class Color(TypedDict):
	name: str
	rgb: List[int]
	hue: int
	saturation: List[int]
	brightness: List[int]
	kelvin: int
