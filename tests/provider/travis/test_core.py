from chroma_feedback.provider.travis.core import fetch


def test_fetch_slug():
	result = fetch('https://api.travis-ci.org', 'redaxmedia/chroma-feedback')

	assert result[0]['provider'] == 'travis'
	assert result[0]['slug'] == 'redaxmedia/chroma-feedback'
	assert result[0]['active'] is True
	assert result[0]['status']


def test_fetch_user():
	result = fetch('https://api.travis-ci.org', 'redaxmedia')

	assert result[0]['provider'] == 'travis'
	assert result[0]['slug']
	assert result[0]['active'] is True
	assert result[0]['status']


def test_fetch_invalid():
	result = fetch(None, None)

	assert result == []
