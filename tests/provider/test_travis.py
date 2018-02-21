from src.provider import travis


def test_travis_slug():
	data = travis.fetch_data('redaxmedia/chroma-feedback')
	assert len(data) == 1


def test_travis_user():
	data = travis.fetch_data('redaxmedia')
	assert len(data) > 1
