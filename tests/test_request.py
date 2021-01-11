from chroma_feedback import request


def test_get() -> None:
	assert request.get('https://api.github.com/repos/redaxmedia/chroma-feedback', None)
