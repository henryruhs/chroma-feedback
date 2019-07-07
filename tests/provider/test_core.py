from argparse import ArgumentParser
import sys
from src import provider

def test_progress(mocker):
	program = ArgumentParser()
	program.add_argument('-P', '--provider', action = 'append', required = True)
	sys.argv.append('--provider')
	sys.argv.append('travis')
	sys.argv.append('--travis-slug')
	sys.argv.append('redaxmedia')
	load = mocker.spy(provider.core, 'load')
	provider.process(program)
	assert load.call_count == 1
