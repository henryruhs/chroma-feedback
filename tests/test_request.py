from chroma_feedback import request


def test_get() -> None:
	assert request.get('invalid', None) is None
	assert request.get('https://api.github.com/repos/redaxmedia/chroma-feedback', None)


def test_post() -> None:
	assert request.post('invalid', None) is None
