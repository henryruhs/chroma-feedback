from src.provider import jenkins


def test_fetch_invalid():
	result = jenkins.fetch(None, None, None)
	assert result == []
