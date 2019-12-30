from typing import Any
from argparse import ArgumentParser
import sys
from chroma_feedback import producer


def test_process(mocker : Any) -> None:
	program = ArgumentParser()
	program.add_argument('-P', '--producer', action = 'append', required = True)
	sys.argv.append('--producer')
	sys.argv.append('travis')
	sys.argv.append('--travis-slug')
	sys.argv.append('redaxmedia')
	process = mocker.spy(producer.travis, 'run')
	producer.process(program)

	assert process.call_count == 1
