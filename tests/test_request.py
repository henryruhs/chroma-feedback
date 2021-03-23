from chroma_feedback import request


def test_get() -> None:
	response = request.get('https://jsonplaceholder.typicode.com/posts',
	{
		'Content-Type': 'application/json'
	})

	assert response.status_code == 200


def test_post() -> None:
	response = request.post('https://jsonplaceholder.typicode.com/posts', headers =
	{
		'Content-Type': 'application/json'
	})

	assert response.status_code == 201
