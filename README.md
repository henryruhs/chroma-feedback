Chroma Feedback
===============

> Turn your RGB powered hardware into an build indicator for continuous integration.

[![Build Status Travis](https://img.shields.io/travis/redaxmedia/chroma-feedback.svg)](https://travis-ci.org/redaxmedia/chroma-feedback)
[![Build Status AppVeyor](https://img.shields.io/appveyor/ci/redaxmedia/chroma-feedback.svg)](https://ci.appveyor.com/project/redaxmedia/chroma-feedback)
[![Coverage Status](https://img.shields.io/coveralls/redaxmedia/chroma-feedback.svg)](https://coveralls.io/r/redaxmedia/chroma-feedback)
[![PyPI](https://img.shields.io/pypi/v/chroma-feedback.svg)](https://pypi.org/project/chroma-feedback)
[![License](https://img.shields.io/pypi/l/chroma-feedback.svg)](https://pypi.org/project/chroma-feedback)
[![Telegram Chat](https://img.shields.io/badge/chat-on_telegram-0088cc.svg)](https://t.me/chroma_feedback)


Preview
-------

![Terminal Session](https://cdn.rawgit.com/redaxmedia/media/master/chroma-feedback/terminal-session.svg)


Installation
------------

Install Chroma Feedback:

```
apt-get install libusb-1.0-0-dev libudev-dev
```

```
pip3 install chroma-feedback
```

Install `openrazer-meta` for Razer Chroma:

```
add-apt-repository ppa:openrazer/stable
apt-get update
```

```
apt install openrazer-meta
```


Usage
-----

Combine producers and consumers as needed:

```
chroma-feedback [options]

-V, --version
-P, --producer <producer>
-C, --consumer <consumer>
-I, --background-interval <background-interval>
-B, --background-run
-D, --dry-run
-h, --help
```


Producers
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
chroma-feedback --producer=appveyor

--appveyor-slug <username/repository>
```

Monitor multiple projects:

```
chroma-feedback --producer=appveyor

--appveyor-token <token>
```


Bamboo
------

| Name     | Mandatory |
|----------|-----------|
| Host     | required  |
| Slug     | required  |
| Username | required  |
| Password | required  |

Monitor a single project:

```
chroma-feedback --producer=bamboo

--bamboo-host <host>
--bamboo-slug <project-key>
--bamboo-username <username>
--bamboo-password <password>
```

Monitor multiple projects:

```
chroma-feedback --producer=bamboo

--bamboo-host <host>
--bamboo-slug <plan>
--bamboo-username <username>
--bamboo-password <password>
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
chroma-feedback --producer=circle

--circle-slug <username/repository>
```

Monitor multiple projects:

```
chroma-feedback --producer=circle

--circle-token <token>
```


Codeship
--------

| Name     | Default                  | Mandatory |
|----------|--------------------------|-----------|
| Host     | https://api.codeship.com | optional  |
| Slug     |                          | optional  |
| Username |                          | required  |
| Password |                          | required  |

Monitor a single project:

```
chroma-feedback --producer=codeship

--codeship-slug <project-id>
--codeship-username <username>
--codeship-password <password>
```

Monitor multiple projects:

```
chroma-feedback --producer=codeship

--codeship-username <username>
--codeship-password <password>
```


Custom
------

| Name     | Mandatory |
|----------|-----------|
| Host     | required  |
| Slug     | required  |

Monitor a single project:

```
chroma-feedback --producer=custom

--custom-host <host>
--custom-slug <slug>
```

Monitor multiple projects:

```
chroma-feedback --producer=custom

--custom-host <host>
--custom-slug <slug>
--custom-slug <slug>
```

Example for `{host}/statuses/{slug}` endpoint:

```
[
	{
		"slug": "chroma-feedback",
		"active": true,
		"status": "passed"
	}
]
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
chroma-feedback --producer=github

--github-slug <username/repository>
--github-username <username>
--github-token <token>
```

Monitor multiple projects:

```
chroma-feedback --producer=github

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
chroma-feedback --producer=gitlab

--gitlab-slug <project-id>
--gitlab-token <token>
```

Monitor multiple projects:

```
chroma-feedback --producer=gitlab

--gitlab-slug <project-id>
--gitlab-slug <project-id>
--gitlab-token <token>
```


Jenkins
-------

| Name     | Mandatory |
|----------|-----------|
| Host     | required  |
| Slug     | required  |
| Username | optional  |
| Password | optional  |

Monitor a single project:

```
chroma-feedback --producer=jenkins

--jenkins-host <host>
--jenkins-slug <job>
--jenkins-username <username>
--jenkins-password <password>
```

Monitor multiple projects:

```
chroma-feedback --producer=jenkins

--jenkins-host <host>
--jenkins-slug <job>
--jenkins-slug <job>
--jenkins-username <username>
--jenkins-password <password>
```


TeamCity
--------

| Name     | Default                        | Mandatory |
|----------|--------------------------------|-----------|
| Host     | https://teamcity.jetbrains.com | optional  |
| Slug     |                                | optional  |
| Token    |                                | required  |

Monitor a single project:

```
chroma-feedback --producer=teamcity

--teamcity-slug <project-id>
--teamcity-token<token>
```

Monitor multiple projects:

```
chroma-feedback --producer=teamcity

--teamcity-token <token>
```


Travis
------

| Name | Default                   | Mandatory |
|------|---------------------------|-----------|
| Host | https://api.travis-ci.org | optional  |
| Slug |                           | required  |

Monitor a single project:

```
chroma-feedback --producer=travis

--travis-slug <username/repository>
```

Monitor multiple projects:

```
chroma-feedback --producer=travis

--travis-slug <username>
```


Wercker
-------

| Name  | Default                 | Mandatory |
|-------|-------------------------|-----------|
| Host  | https://app.wercker.com | optional  |
| Slug  |                         | required  |
| Token |                         | required  |

Monitor a single project:

```
chroma-feedback --producer=wercker

--wercker-slug <username/application>
--wercker-token <token>
```

Monitor multiple projects:

```
chroma-feedback --producer=wercker

--wercker-slug <<username/application>
--wercker-slug <<username/application>
--wercker-token <token>
```


Consumers
=========


Agile Innovative BlinkStick
---------------------------

| Name   | Mandatory |
|--------|-----------|
| Device | optional  |

Indicate status via devices:

```
chroma-feedback --consumer=agile_innovative_blinkstick

--agile-innovative-blinkstick-device <device-serial>
```


Lifx Light
----------

| Name     | Mandatory |
|----------|-----------|
| Light    | optional  |
| Group    | optional  |

Indicate status via lights:

```
chroma-feedback --consumer=lifx_light

--lifx-light-light <light-name>
```

Indicate status via groups:

```
chroma-feedback --consumer=lifx_light

--lifx-light-group <group-name>
```


Magic Hue
---------

| Name     | Mandatory |
|----------|-----------|
| IP       | optional  |

Indicate status via lights:

```
chroma-feedback --consumer=magic_hue
```


Philips Hue
-----------

| Name     | Mandatory |
|----------|-----------|
| IP       | optional  |
| Light    | optional  |
| Group    | optional  |

Indicate status via lights:

```
chroma-feedback --consumer=philips_hue

--philips-hue-light <light-name>
```

Indicate status via groups:

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

Indicate status via devices:

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
