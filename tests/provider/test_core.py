from argparse import ArgumentParser
import sys
from chroma_feedback import provider

def test_process(mocker):
	program = ArgumentParser()
	program.add_argument('-P', '--provider', action = 'append', required = True)
	sys.argv.append('--provider')
	sys.argv.append('travis')
	sys.argv.append('--travis-slug')
	sys.argv.append('redaxmedia')
	process = mocker.spy(provider.travis, 'run')
	provider.process(program)
	assert process.call_count == 1
