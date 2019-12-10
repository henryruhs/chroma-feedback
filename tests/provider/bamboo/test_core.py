from chroma_feedback.provider.bamboo.core import fetch


def test_fetch_invalid() -> None:
	result = fetch(None, None, None, None)

	assert result == []
