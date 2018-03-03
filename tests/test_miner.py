from unittest.mock import MagicMock
from src import miner


def test_progress(mocker):
	args = MagicMock()
	args.provider = 'appveyor, circle, gitlab, jenkins, teamcity, travis'
	args.slug = 'redaxmedia/chroma-feedback'
	fetch = mocker.spy(miner, 'fetch')
	miner.process(args)
	assert fetch.call_count == 1326
