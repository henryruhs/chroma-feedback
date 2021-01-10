from typing import Any, Dict, List
from argparse import ArgumentParser
import importlib
from chroma_feedback import helper, wording


def process(program : ArgumentParser) -> List[Dict[str, Any]]:
	args = helper.get_first(program.parse_known_args())
	result = []

	for producer_name in args.producer:
		producer = load_producer(producer_name)
		producer.init(program)
		try:
			result.extend(producer.run())
		except:
			exit(wording.get('producer_crash').format(producer_name) + wording.get('exclamation_mark'))
	return result


def load_producer(producer_name : str) -> Any:
	try:
		return importlib.import_module('chroma_feedback.producer.' + producer_name)
	except ImportError:
		exit(wording.get('producer_no').format(producer_name) + wording.get('exclamation_mark'))
