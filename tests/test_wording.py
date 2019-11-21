from chroma_feedback import wording


def test_get() -> None:
	assert wording.get('goodbye') == 'Goodbye'
