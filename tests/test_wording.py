import src.wording as wording


def test_get():
	assert wording.get('goodbye') == 'Goodbye'
