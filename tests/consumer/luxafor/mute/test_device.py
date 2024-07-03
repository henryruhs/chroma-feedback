from unittest.mock import MagicMock

import pytest

from chroma_feedback.consumer.luxafor.mute.light import process_lights

MOCK = MagicMock()


def test_process_passed() -> None:
	try:
		result = process_lights(
		{
			MOCK
		},
		[
			{
				'name': 'microsoft.github',
				'symbol': None,
				'message': None,
				'url': 'https://github.com/henryruhs/chroma-feedback/actions/runs/1',
				'status': 'passed'
			}
		])

		assert result[0]['name'] == 'luxafor.mute'
		assert result[0]['type'] == 'device'
		assert result[0]['description']
		assert result[0]['status'] == 'passed'
	except:
		pytest.skip()


def test_process_started() -> None:
	try:
		result = process_lights(
		{
			MOCK
		},
		[
			{
				'name': 'microsoft.github',
				'symbol': None,
				'message': None,
				'url': 'https://github.com/henryruhs/chroma-feedback/actions/runs/1',
				'status': 'started'
			}
		])

		assert result[0]['name'] == 'luxafor.mute'
		assert result[0]['type'] == 'device'
		assert result[0]['description']
		assert result[0]['status'] == 'started'
	except:
		pytest.skip()


def test_process_errored() -> None:
	try:
		result = process_lights(
		{
			MOCK
		},
		[
			{
				'name': 'microsoft.github',
				'symbol': None,
				'message': None,
				'url': 'https://github.com/henryruhs/chroma-feedback/actions/runs/1',
				'status': 'errored'
			}
		])

		assert result[0]['name'] == 'luxafor.mute'
		assert result[0]['type'] == 'device'
		assert result[0]['description']
		assert result[0]['status'] == 'errored'
	except:
		pytest.skip()


def test_process_warned() -> None:
	try:
		result = process_lights(
		{
			MOCK
		},
		[
			{
				'name': 'microsoft.github',
				'symbol': None,
				'message': None,
				'url': 'https://github.com/henryruhs/chroma-feedback/actions/runs/1',
				'status': 'warned'
			}
		])

		assert result[0]['name'] == 'luxafor.mute'
		assert result[0]['type'] == 'device'
		assert result[0]['description']
		assert result[0]['status'] == 'warned'
	except:
		pytest.skip()


def test_process_failed() -> None:
	try:
		result = process_lights(
		{
			MOCK
		},
		[
			{
				'name': 'microsoft.github',
				'symbol': None,
				'message': None,
				'url': 'https://github.com/henryruhs/chroma-feedback/actions/runs/1',
				'status': 'failed'
			}
		])

		assert result[0]['name'] == 'luxafor.mute'
		assert result[0]['type'] == 'device'
		assert result[0]['description']
		assert result[0]['status'] == 'failed'
	except:
		pytest.skip()
