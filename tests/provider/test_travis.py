from src.provider import travis


def test_fetch_data_slug():
	data = travis.fetch_data('redaxmedia/chroma-feedback')
	assert data[0]['provider'] == 'travis'
	assert data[0]['slug'] == 'redaxmedia/chroma-feedback'
	assert data[0]['active'] is True
	assert data[0]['status']


def test_fetch_data_user():
	data = travis.fetch_data('redaxmedia')
	assert data[0]['provider'] == 'travis'
	assert data[0]['active'] is True
	assert data[0]['status']
