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


def test_parse_json() -> None:
	response = request.post('https://jsonplaceholder.typicode.com/posts', headers =
	{
		'Content-Type': 'application/json'
	})
	data = request.parse_json(response)

	assert data['id']


def test_create_basic_auth_headers() -> None:
	headers = request.create_basic_auth_headers('abc', '12345')

	assert headers['Accept'] == 'application/json'
	assert headers['Authorization'] == 'Basic YWJjOjEyMzQ1'


def test_create_bearer_auth_headers() -> None:
	headers = request.create_bearer_auth_headers('12345')

	assert headers['Accept'] == 'application/json'
	assert headers['Authorization'] == 'Bearer 12345'
