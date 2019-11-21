from chroma_feedback import metadata


def test_get() -> None:
	assert metadata.get('name') == 'chroma-feedback'
