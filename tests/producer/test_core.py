import os
import sys
from argparse import ArgumentParser
from typing import Any

import pytest

from chroma_feedback import producer


def test_process(mocker : Any) -> None:
	if os.environ.get('TRAVIS_TOKEN'):
		program = ArgumentParser()
		program.add_argument('-P', '--producer', action = 'append', choices = producer.ALL, required = True)
		sys.argv.append('--producer')
		sys.argv.append('travis')
		sys.argv.append('--travis-slug')
		sys.argv.append('henryruhs/chroma-feedback')
		sys.argv.append('--travis-token')
		sys.argv.append(os.environ.get('TRAVIS_TOKEN'))
		process = mocker.spy(producer.travis.travis, 'run')
		producer.process(program)

		assert process.call_count == 1
	else:
		pytest.skip('TRAVIS_TOKEN is not defined')
