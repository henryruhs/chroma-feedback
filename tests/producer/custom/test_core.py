from chroma_feedback.producer.custom.core import fetch


def test_fetch_invalid() -> None:
	result = fetch(None, None)

	assert result == []
