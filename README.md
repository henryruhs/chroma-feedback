Chroma Feedback
===============

> Turn your Razer keyboard, mouse or headphone into a extreme feedback device.

[![Build Status Travis](https://img.shields.io/travis/redaxmedia/chroma-feedback.svg)](https://travis-ci.org/redaxmedia/chroma-feedback)
[![Build Status AppVeyor](https://img.shields.io/appveyor/ci/redaxmedia/chroma-feedback.svg)](https://ci.appveyor.com/project/redaxmedia/chroma-feedback)
[![Build Status Circle](https://img.shields.io/circleci/project/github/redaxmedia/chroma-feedback.svg)](https://circleci.com/gh/redaxmedia/chroma-feedback)
[![Coverage Status](https://img.shields.io/coveralls/redaxmedia/chroma-feedback.svg)](https://coveralls.io/r/redaxmedia/chroma-feedback)
[![PyPI](https://img.shields.io/pypi/v/chroma-feedback.svg)](https://pypi.org/project/chroma-feedback)
[![License](https://img.shields.io/pypi/l/chroma-feedback.svg)](https://pypi.org/project/chroma-feedback)


Preview
-------

![Terminal Session](https://cdn.rawgit.com/redaxmedia/media/master/chroma-feedback/terminal-session.svg)


Installation
------------

Install Chroma Feedback using PyPI:

```
pip3 install chroma-feedback
```


Usage
-----

```
chroma-feedback [options]

-V, --version
-P, --provider <provider>
-C, --consumer <consumer>
-I, --background-interval <background-interval>
-B, --background-run
-D, --dry-run
-h, --help
```


Providers
=========


AppVeyor
--------

| Name  | Default                 | Mandatory |
|-------|-------------------------|-----------|
| Host  | https://ci.appveyor.com | optional  |
| Slug  |                         | optional  |
| Token |                         | optional  |

Monitor a single project:

```
chroma-feedback --provider=appveyor --appveyor-slug={USERNAME/REPOSITORY}
```

Monitor multiple projects:

```
chroma-feedback --provider=appveyor --appveyor-token={TOKEN}
```


Circle
------

| Name  | Default              | Mandatory |
|-------|----------------------|-----------|
| Host  | https://circleci.com | optional  |
| Slug  |                      | optional  |
| Token |                      | optional  |

Monitor a single project:

```
chroma-feedback --provider=circle --circle-slug={USERNAME/REPOSITORY}
```

Monitor multiple projects:

```
chroma-feedback --provider=circle --circle-token={TOKEN}
```


GitHub
------

| Name     | Default                | Mandatory |
|----------|------------------------|-----------|
| Host     | https://api.github.com | optional  |
| Slug     |                        | required  |
| Username |                        | required  |
| Token    |                        | required  |

Monitor a single project:

```
chroma-feedback --provider=github --github-slug={USERNAME/REPOSITORY} --github-username={USERNAME} --github-token={TOKEN}
```

Monitor multiple projects:

```
chroma-feedback --provider=github --github-slug={USERNAME/REPOSITORY} --github-slug={USERNAME/REPOSITORY} --github-username={USERNAME} --github-token={TOKEN}
```


GitLab
------

| Name  | Default            | Mandatory |
|-------|--------------------|-----------|
| Host  | https://gitlab.com | optional  |
| Slug  |                    | required  |
| Token |                    | required  |

Monitor a single project:

```
chroma-feedback --provider=gitlab --gitlab-slug={PROJECT-ID}--gitlab-token={TOKEN}
```

Monitor multiple projects:

```
chroma-feedback --provider=gitlab --gitlab-slug={PROJECT-ID} --gitlab-slug={PROJECT-ID} --gitlab-token={TOKEN}
```


Jenkins
-------

| Name | Default | Mandatory |
|------|---------|-----------|
| Host |         | required  |
| Slug |         | required  |

Monitor a single project:

```
chroma-feedback --provider=jenkins --jenkins-host={HOST} --jenkins-slug={JOB-NAME}
```

Monitor multiple projects:

```
chroma-feedback --provider=jenkins --jenkins-host={HOST} --jenkins-slug={JOB-NAME} --jenkins-slug={JOB-NAME}
```


TeamCity
--------

| Name     | Default                        | Mandatory |   |
|----------|--------------------------------|-----------|---|
| Host     | https://teamcity.jetbrains.com | optional  |   |
| Slug     |                                | optional  |   |
| Username |                                | required  |   |
| Password |                                | required  |   |

Monitor a single project:

```
chroma-feedback --provider=teamcity --teamcity-slug={SLUG} --teamcity-username={USERNAME} --teamcity-password={PASSWORD}
```

Monitor multiple projects:

```
chroma-feedback --provider=teamcity --teamcity-username={USERNAME} --teamcity-password={PASSWORD}
```


Travis
------

| Name | Default                   | Mandatory |
|------|---------------------------|-----------|
| Host | https://api.travis-ci.org | optional  |
| Slug |                           | required  |

Monitor a single project:

```
chroma-feedback --provider=travis --travis-slug={USERNAME/REPOSITORY}
```

Monitor multiple projects:

```
chroma-feedback --provider=travis --travis-slug={USERNAME}
```
