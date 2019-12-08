from chroma_feedback.provider.teamcity.core import fetch


def test_fetch_invalid() -> None:
	result = fetch(None, None, None)

	assert result == []
