from chroma_feedback import helper


def test_to_lower_case() -> None:
	assert helper.to_lower_case(None) == 'none'
	assert helper.to_lower_case('SUCCESS') == 'success'