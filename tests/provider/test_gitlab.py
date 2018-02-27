from src.provider import gitlab


def test_fetch_invalid():
	data = gitlab.fetch(None, None, None)
	assert data == []