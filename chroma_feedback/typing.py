from typing import Literal, TypedDict, List

StatusType = Literal['passed', 'started', 'errored', 'failed']


class ProducerModel(TypedDict):
	producer: str
	slug: str
	active: bool
	status: StatusType


class ConsumerModel(TypedDict):
	consumer: str
	type: Literal['light', 'device', 'group']
	name: str
	active: bool
	status: StatusType


class ReportModel(TypedDict):
	status : StatusType
	message : str
	symbol : str


class ColorConfigModel(TypedDict):
	name: str
	rgb: List[int]
	hue: int
	saturation: List[int]
	brightness: List[int]
	kelvin: int
