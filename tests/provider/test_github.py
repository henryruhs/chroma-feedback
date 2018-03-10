from src.provider import github


def test_fetch_slug():
	data = github.fetch(None, 'redaxmedia/chroma-feedback', 'test')
	assert data[0]['provider'] == 'github'
	assert data[0]['slug'] == 'redaxmedia/chroma-feedback'
	assert data[0]['active'] is True
	assert data[0]['status']


def test_fetch_invalid():
	data = github.fetch(None, None, None)
	assert data == []
