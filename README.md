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

Combine providers and consumers as needed:

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


Consumers
=========


Philips Hue
-----------

| Name     | Default                       | Mandatory |
|----------|-------------------------------|-----------|
| Host     | https://discovery.meethue.com | optional  |
| Username |                               | required  |
| Group    |                               | required  |

Indicate via `Philips Hue` lights:

```
chroma-feedback --consumer=philips_hue

--philips-hue-username <username>
--philips-hue-group <group-id>
```


Razer Chroma
------------

Indicate via `Razer Chroma` devices:

```
chroma-feedback --consumer=razer_chroma
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
chroma-feedback --provider=appveyor

--appveyor-slug <username/repository>
```

Monitor multiple projects:

```
chroma-feedback --provider=appveyor

--appveyor-token <token>
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
chroma-feedback --provider=circle

--circle-slug <username/repository>
```

Monitor multiple projects:

```
chroma-feedback --provider=circle

--circle-token <token>
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
chroma-feedback --provider=github

--github-slug <username/repository>
--github-username <username>
--github-token <token>
```

Monitor multiple projects:

```
chroma-feedback --provider=github

--github-slug <username/repository>
--github-slug <username/repository>
--github-username <username>
--github-token <token>
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
chroma-feedback --provider=gitlab

--gitlab-slug <project-id>
--gitlab-token <token>
```

Monitor multiple projects:

```
chroma-feedback --provider=gitlab

--gitlab-slug <project-id>
--gitlab-slug <project-id>
--gitlab-token <token>
```


Jenkins
-------

| Name | Mandatory |
|------|-----------|
| Host | required  |
| Slug | required  |

Monitor a single project:

```
chroma-feedback --provider=jenkins

--jenkins-host <host>
--jenkins-slug <job>
```

Monitor multiple projects:

```
chroma-feedback --provider=jenkins

--jenkins-host <host>
--jenkins-slug <job>
--jenkins-slug <job>
```


TeamCity
--------

| Name     | Default                        | Mandatory |
|----------|--------------------------------|-----------|
| Host     | https://teamcity.jetbrains.com | optional  |
| Slug     |                                | optional  |
| Username |                                | required  |
| Password |                                | required  |

Monitor a single project:

```
chroma-feedback --provider=teamcity

--teamcity-slug <project-id>
--teamcity-username <username>
--teamcity-password <password>
```

Monitor multiple projects:

```
chroma-feedback --provider=teamcity

--teamcity-username <username>
--teamcity-password <password>
```


Travis
------

| Name | Default                   | Mandatory |
|------|---------------------------|-----------|
| Host | https://api.travis-ci.org | optional  |
| Slug |                           | required  |

Monitor a single project:

```
chroma-feedback --provider=travis

--travis-slug <username/repository>
```

Monitor multiple projects:

```
chroma-feedback --provider=travis

--travis-slug <username>
```
