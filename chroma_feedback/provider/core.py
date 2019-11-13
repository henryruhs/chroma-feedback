from typing import Any, Dict, List
from argparse import ArgumentParser
import importlib
from chroma_feedback import helper, wording


def process(program : ArgumentParser) -> List[Dict[str, Any]]:
	args = helper.get_first(program.parse_known_args())
	result = []

	for provider_name in args.provider:
		try:
			provider = importlib.import_module('chroma_feedback.provider.' + provider_name)
			provider.init(program)
			result.extend(provider.run())
		except ImportError:
			exit(wording.get('provider_no') + wording.get('exclamation_mark'))
	return result
