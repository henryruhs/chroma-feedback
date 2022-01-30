from typing import Any
from argparse import ArgumentParser
import sys
import os
import pytest
from chroma_feedback import producer


def test_process(mocker : Any) -> None:
	if os.environ.get('TRAVIS_TOKEN'):
		program = ArgumentParser()
		program.add_argument('-P', '--producer', action = 'append', choices = producer.__all__, required = True)
		sys.argv.append('--producer')
		sys.argv.append('travis')
		sys.argv.append('--travis-slug')
		sys.argv.append('redaxmedia/chroma-feedback')
		sys.argv.append('--travis-token')
		sys.argv.append(os.environ.get('TRAVIS_TOKEN'))
		process = mocker.spy(producer.travis, 'run') # type: ignore
		producer.process(program)

		assert process.call_count == 1
	else:
		pytest.skip('TRAVIS_TOKEN is not defined')
