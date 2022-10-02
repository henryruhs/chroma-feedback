from .core import process

ALL = \
{
	'appveyor': 'chroma_feedback.producer.appveyor.appveyor',
	'atlassian.bamboo': 'chroma_feedback.producer.atlassian.bamboo',
	'atlassian.bitbucket': 'chroma_feedback.producer.atlassian.bitbucket',
	'buddy': 'chroma_feedback.producer.buddy.buddy',
	'circle': 'chroma_feedback.producer.circle.circle',
	'cloudbees.codeship': 'chroma_feedback.producer.cloudbees.codeship',
	'custom': 'chroma_feedback.producer.custom.custom',
	'datadog': 'chroma_feedback.producer.datadog.datadog',
	'gitlab': 'chroma_feedback.producer.gitlab.gitlab',
	'heroku': 'chroma_feedback.producer.heroku.heroku',
	'jenkins': 'chroma_feedback.producer.jenkins.jenkins',
	'jetbrains.teamcity': 'chroma_feedback.producer.jetbrains.teamcity',
	'microsoft.azure': 'chroma_feedback.producer.microsoft.azure',
	'microsoft.github': 'chroma_feedback.producer.microsoft.github',
	'netlify': 'chroma_feedback.producer.netlify.netlify',
	'travis': 'chroma_feedback.producer.travis.travis',
	'vercel': 'chroma_feedback.producer.vercel.vercel'
}
