from src import wording


def test_get():
	assert wording.get('goodbye') == 'Goodbye'
