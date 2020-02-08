import os
import pytest
from chroma_feedback.producer.bamboo.core import fetch

# NOTE: Because Bamboo is a commercial server/datacenter product, there
# are no public instances to run against.  A local trial version can be
# downloaded using the Atlassian SDK or installed via batch script.
# To test against a private instance, this procedure should work:
# - Download and install a trial version of Bamboo.  The setup wizard
#   will prompt to create an admin user.  Name it 'redaxmedia', then
#   choose a password.
# - Create a project named 'redaxmedia' with key 'REDAXMEDIA'.
# - In that project, create two plans:
#   - 'chroma-feedback' with key 'CF';
#   - 'bamboo-producer' with key 'BP'.
# - Configure each plan to do a trivial task such as an echo statement.
# - Run both plans so that they have a build status.
#
# At this point the tests can be run.  Provide the following envvars:
# - BAMBOO_HOST : The URL of the Bamboo installation.
# - BAMBOO_TOKEN: The password of the administrator user.

def test_fetch_project_slug() -> None:
	if ('BAMBOO_TOKEN' in os.environ) and ('BAMBOO_HOST' in os.environ):
		result = fetch(os.environ['BAMBOO_HOST'], 'REDAXMEDIA', 'redaxmedia', os.environ['BAMBOO_TOKEN'])

		assert result[0]['producer'] == 'bamboo'
		assert 'REDAXMEDIA' in result[0]['slug']
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('BAMBOO_USER and BAMBOO_TOKEN must be defined.')

def test_fetch_plan_slug() -> None:
	if ('BAMBOO_TOKEN' in os.environ) and ('BAMBOO_HOST' in os.environ):
		result = fetch(os.environ['BAMBOO_HOST'], 'REDAXMEDIA-CF', 'redaxmedia', os.environ['BAMBOO_TOKEN'])

		assert result[0]['producer'] == 'bamboo'
		assert 'REDAXMEDIA-CF' in result[0]['slug']
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('BAMBOO_USER and BAMBOO_TOKEN must be defined.')

def test_fetch_invalid() -> None:
	result = fetch(None, None, None, None)

	assert result == []
