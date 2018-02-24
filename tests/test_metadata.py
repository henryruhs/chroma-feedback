from src import metadata


def test_get():
	assert metadata.get('name') == 'chroma-feedback'
