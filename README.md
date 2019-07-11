Chroma Feedback
===============

> Turn your RGB powered hardware into an extreme feedback device for continuous integration.

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

Install Chroma Feedback:

```
pip3 install chroma-feedback
```

Install `phue` for Philips Hue:

```
pip3 install phue
```

Install `openrazer-meta` for Razer Chroma:

```
add-apt-repository ppa:openrazer/stable
apt-get update
```

```
apt install openrazer-meta
```

Install `blink1` for ThingM Blink:

```
apt-get install libusb-dev libudev-dev
```

```
pip3 install blink1
```

Install `yeelight` for Xiaomi Yeelight:

```
pip3 install yeelight
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
| IP       | optional  |
| Group    | optional  |

Indicate status via lights:

```
chroma-feedback --consumer=philips_hue

--philips-hue-group <group-name>
```


Razer Chroma
------------

| Name   | Mandatory |
|--------|-----------|
| Device | optional  |

Indicate status via devices:

```
chroma-feedback --consumer=razer_chroma

--razer-chrome-device <device-name>
```


ThingM Blink
------------

| Name   | Mandatory |
|--------|-----------|
| Device | optional  |

Indicate status via lights:

```
chroma-feedback --consumer=thingm_blink

--thingm-blink-device <device-serial>
```


Xiaomi Yeelight
---------------

| Name     | Mandatory |
|----------|-----------|
| IP       | optional  |

Indicate status via lights:

```
chroma-feedback --consumer=xiaomi_yeelight
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
