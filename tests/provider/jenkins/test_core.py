from chroma_feedback.provider import jenkins


def test_fetch_invalid():
	result = jenkins.fetch(None, None)

	assert result == []
