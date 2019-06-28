from src.provider import teamcity


def test_fetch_invalid():
	result = teamcity.fetch(None, None, None)
	assert result == []
