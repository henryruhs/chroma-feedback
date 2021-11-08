from typing import Literal, TypedDict, List

Status = Literal['passed', 'started', 'errored', 'failed']


class Producer(TypedDict):
	producer: str
	slug: str
	active: bool
	status: Status


class Consumer(TypedDict):
	consumer: str
	type: Literal['light', 'device', 'group']
	name: str
	active: bool
	status: Status


class Report(TypedDict):
	status : Status
	message : str
	symbol : str


class Color(TypedDict):
	name: str
	rgb: List[int]
	hue: int
	saturation: List[int]
	brightness: List[int]
	kelvin: int
