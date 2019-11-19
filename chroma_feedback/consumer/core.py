from typing import Any, Dict, List
from argparse import ArgumentParser
import importlib
from chroma_feedback import wording


def process(program : ArgumentParser, status : str) -> List[Dict[str, Any]]:
	args = program.parse_known_args()[0]
	result = []

	for consumer_name in args.consumer:
		try:
			consumer = importlib.import_module('chroma_feedback.consumer.' + consumer_name)
			consumer.init(program)
			result.extend(consumer.run(status))
		except ImportError:
			exit(wording.get('consumer_no') + wording.get('exclamation_mark'))
	return result
