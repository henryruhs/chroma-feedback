from chroma_feedback import metadata


def test_get():
	assert metadata.get('name') == 'chroma-feedback'
