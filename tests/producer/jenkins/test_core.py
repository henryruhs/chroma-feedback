from chroma_feedback.producer.jenkins.core import fetch


def test_fetch_invalid() -> None:
	result = fetch(None, None, None, None)

	assert result == []
