from src.provider import jenkins


def test_fetch_invalid():
	data = jenkins.fetch(None, None)
	assert data == []