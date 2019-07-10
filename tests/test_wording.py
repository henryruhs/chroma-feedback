from chroma_feedback import wording


def test_get():
	assert wording.get('goodbye') == 'Goodbye'
