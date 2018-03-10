from src.provider import teamcity


def test_fetch_invalid():
	data = teamcity.fetch(None, None, None)
	assert data == []
