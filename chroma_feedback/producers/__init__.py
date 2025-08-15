from .core import process

ALL = \
{
	'appveyor': 'chroma_feedback.producers.appveyor.appveyor',
	'atlassian.bamboo': 'chroma_feedback.producers.atlassian.bamboo',
	'atlassian.bitbucket': 'chroma_feedback.producers.atlassian.bitbucket',
	'betterstack': 'chroma_feedback.producers.betterstack.betterstack',
	'buddy': 'chroma_feedback.producers.buddy.buddy',
	'circle': 'chroma_feedback.producers.circle.circle',
	'cloudbees.codeship': 'chroma_feedback.producers.cloudbees.codeship',
	'custom': 'chroma_feedback.producers.custom.custom',
	'datadog': 'chroma_feedback.producers.datadog.datadog',
	'gitlab': 'chroma_feedback.producers.gitlab.gitlab',
	'heroku': 'chroma_feedback.producers.heroku.heroku',
	'jenkins': 'chroma_feedback.producers.jenkins.jenkins',
	'jetbrains.teamcity': 'chroma_feedback.producers.jetbrains.teamcity',
	'microsoft.azure': 'chroma_feedback.producers.microsoft.azure',
	'microsoft.github': 'chroma_feedback.producers.microsoft.github',
	'netlify': 'chroma_feedback.producers.netlify.netlify',
	'travis': 'chroma_feedback.producers.travis.travis',
	'uptimerobot': 'chroma_feedback.producers.uptimerobot.uptimerobot',
	'vercel': 'chroma_feedback.producers.vercel.vercel'
}
