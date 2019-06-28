import src.provider.jenkins.core as jenkins


def test_fetch_invalid():
	result = jenkins.fetch(None, None)
	assert result == []
