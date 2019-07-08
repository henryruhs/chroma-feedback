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

| Name     | Mandatory |
|----------|-----------|
| Host     | required  |
| Username | required  |
| Group    | required  |

Update by group:

```
chroma-feedback --consumer=philips_hue [options]

--philips-hue-host <host>
--philips-hue-username <username>
--philips-hue-group <group-id>
```


Razer Chroma
------------

Update connected devices:

```
chroma-feedback --consumer=razer_chroma
```


System Tray
-----------

Show interactive system tray:

```
chroma-feedback --consumer=system_tray
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
chroma-feedback --provider=appveyor [options]

--appveyor-slug <username/repository>
```

Monitor multiple projects:

```
chroma-feedback --provider=appveyor [options]

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
chroma-feedback --provider=circle [options]

--circle-slug <username/repository>
```

Monitor multiple projects:

```
chroma-feedback --provider=circle [options]

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
chroma-feedback --provider=github [options]

--github-slug <username/repository>
--github-username <username>
--github-token <token>
```

Monitor multiple projects:

```
chroma-feedback --provider=github [options]

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
chroma-feedback --provider=gitlab [options]

--gitlab-slug <project-id>
--gitlab-token <token>
```

Monitor multiple projects:

```
chroma-feedback --provider=gitlab [options]

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
chroma-feedback --provider=jenkins [options]

--jenkins-host <host>
--jenkins-slug <job>
```

Monitor multiple projects:

```
chroma-feedback --provider=jenkins [options]

--jenkins-host <host>
--jenkins-slug <job-name>
--jenkins-slug <job-name>
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
chroma-feedback --provider=teamcity [options]

--teamcity-slug <project-id>
--teamcity-username <username>
--teamcity-password <password>
```

Monitor multiple projects:

```
chroma-feedback --provider=teamcity [options]

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
chroma-feedback --provider=travis [options]

--travis-slug <username/repository>
```

Monitor multiple projects:

```
chroma-feedback --provider=travis [options]

--travis-slug <username>
```
