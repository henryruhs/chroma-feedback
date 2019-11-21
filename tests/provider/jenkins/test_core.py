from chroma_feedback.provider.jenkins.core import fetch


def test_fetch_invalid() -> None:
	result = fetch(None, None)

	assert result == []
