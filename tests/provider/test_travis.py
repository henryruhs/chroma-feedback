from src.provider import travis


def test_fetch_data_slug():
	data = travis.fetch_data('redaxmedia/chroma-feedback')
	assert len(data) == 1


def test_fetch_data_user():
	data = travis.fetch_data('redaxmedia')
	assert len(data) > 0
