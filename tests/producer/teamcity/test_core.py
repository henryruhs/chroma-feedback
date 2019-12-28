from chroma_feedback.producer.teamcity.core import fetch


def test_fetch_invalid() -> None:
	result = fetch(None, None, None)

	assert result == []
