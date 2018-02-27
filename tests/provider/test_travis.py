from src.provider import travis


def test_fetch_slug():
	data = travis.fetch(None, 'redaxmedia/chroma-feedback')
	assert data[0]['provider'] == 'travis'
	assert data[0]['slug'] == 'redaxmedia/chroma-feedback'
	assert data[0]['active'] is True
	assert data[0]['status']


def test_fetch_user():
	data = travis.fetch(None, 'redaxmedia')
	assert data[0]['provider'] == 'travis'
	assert data[0]['active'] is True
	assert data[0]['status']


def test_fetch_invalid():
	data = travis.fetch(None, None)
	assert data == []
