from chroma_feedback.producer.bitbucket.core import fetch


def test_fetch_slug() -> None:
	result = fetch('https://api.bitbucket.org', 'redaxmedia/test-dummy')

	assert result[0]['producer'] == 'bitbucket'
	assert result[0]['slug'] == 'redaxmedia/test-dummy'
	assert result[0]['active'] is True
	assert result[0]['status']


def test_fetch_invalid() -> None:
	result = fetch(None, None)

	assert result == []
