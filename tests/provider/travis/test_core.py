from src.provider import travis


def test_fetch_slug():
	result = travis.fetch('https://api.travis-ci.org', 'redaxmedia/chroma-feedback')
	print(result)
	assert result[0]['provider'] == 'travis'
	assert result[0]['slug'] == 'redaxmedia/chroma-feedback'
	assert result[0]['active'] is True
	assert result[0]['status']


def test_fetch_user():
	result = travis.fetch('https://api.travis-ci.org', 'redaxmedia')
	assert result[1]['provider'] == 'travis'
	assert result[1]['active'] is True
	assert result[1]['status']


def test_fetch_invalid():
	result = travis.fetch(None, None)
	assert result == []
