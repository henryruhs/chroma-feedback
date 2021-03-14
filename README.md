Chroma Feedback
===============

> Turn your RGB powered hardware into an build indicator for continuous integration.

[![Build Status](https://img.shields.io/github/workflow/status/redaxmedia/chroma-feedback/ci.svg)](https://github.com/redaxmedia/chroma-feedback/actions?query=workflow:ci)
[![Coverage Status](https://img.shields.io/coveralls/redaxmedia/chroma-feedback.svg)](https://coveralls.io/r/redaxmedia/chroma-feedback)
[![PyPI](https://img.shields.io/pypi/v/chroma-feedback.svg)](https://pypi.org/project/chroma-feedback)
[![License](https://img.shields.io/pypi/l/chroma-feedback.svg)](https://pypi.org/project/chroma-feedback)


Preview
-------

![Terminal Session](https://raw.githubusercontent.com/redaxmedia/chroma-feedback/master/.github/terminal-session.svg?sanitize=true)


Installation
------------

Install Chroma Feedback:

```
apt-get install gir1.2-appindicator3-0.1 libusb-1.0-0-dev libudev-dev
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
| Token |                         | required  |

Monitor a single build:

```
chroma-feedback --producer=appveyor

--appveyor-slug <username/repository>
--appveyor-token <token>
```

Monitor multiple builds:

```
chroma-feedback --producer=appveyor

--appveyor-token <token>
```


Bamboo
------

| Name  | Mandatory |
|-------|-----------|
| Host  | required  |
| Slug  | required  |
| Token | required  |

Monitor a single build:

```
chroma-feedback --producer=bamboo

--bamboo-host <host>
--bamboo-slug <plan>
--bamboo-token <token>
```

Monitor multiple builds:

```
chroma-feedback --producer=bamboo

--bamboo-host <host>
--bamboo-slug <project>
--bamboo-token <token>
```


Bitbucket
---------

| Name     | Default                   | Mandatory |
|----------|---------------------------|-----------|
| Host     | https://api.bitbucket.org | optional  |
| Slug     |                           | required  |
| Username |                           | required  |
| Password |                           | required  |

Monitor a single build:

```
chroma-feedback --producer=bitbucket

--bitbucket-slug <username/repository>
--bitbucket-username <username>
--bitbucket-password <password>
```

Monitor multiple builds:

```
chroma-feedback --producer=bitbucket

--bitbucket-slug <username/repository>
--bitbucket-slug <username/repository>
--bitbucket-username <username>
--bitbucket-password <password>
```


Circle
------

| Name         | Default              | Mandatory |
|--------------|----------------------|-----------|
| Host         | https://circleci.com | optional  |
| Organization |                      | optional  |
| Slug         |                      | optional  |
| Filter       |                      | optional  |
| Token        |                      | required  |

Monitor a single build:

```
chroma-feedback --producer=circle

--circle-slug <username/repository>
--circle-token <token>
```

Monitor multiple builds with `mine` filter:

```
chroma-feedback --producer=circle
--circle-slug <username/repository>
--circle-slug <username/repository>
--circle-filter=mine
--circle-token <token>
```

Monitor multiple builds:

```
chroma-feedback --producer=circle

--circle-organization <organization>
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

Monitor a single build:

```
chroma-feedback --producer=codeship

--codeship-slug <username/repository>
--codeship-username <username>
--codeship-password <password>
```

Monitor multiple builds:

```
chroma-feedback --producer=codeship

--codeship-username <username>
--codeship-password <password>
```


Custom
------

| Name | Mandatory |
|------|-----------|
| Host | required  |
| Slug | required  |

Monitor a single build:

```
chroma-feedback --producer=custom

--custom-host <host>
--custom-slug <slug>
```

Monitor multiple builds:

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

| Name  | Default                | Mandatory |
|-------|------------------------|-----------|
| Host  | https://api.github.com | optional  |
| Slug  |                        | required  |
| Token |                        | required  |

Monitor a single build:

```
chroma-feedback --producer=github

--github-slug <username/repository>
--github-token <token>
```

Monitor multiple builds:

```
chroma-feedback --producer=github

--github-slug <username>
--github-token <token>
```


GitLab
------

| Name  | Default            | Mandatory |
|-------|--------------------|-----------|
| Host  | https://gitlab.com | optional  |
| Slug  |                    | required  |
| Token |                    | required  |

Monitor a single build:

```
chroma-feedback --producer=gitlab

--gitlab-slug <project-id>
--gitlab-token <token>
```

Monitor multiple builds:

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
| Username | required  |
| Password | required  |

Monitor a single build:

```
chroma-feedback --producer=jenkins

--jenkins-host <host>
--jenkins-slug <job>
--jenkins-username <username>
--jenkins-password <password>
```

Monitor multiple builds:

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

| Name  | Default                        | Mandatory |
|-------|--------------------------------|-----------|
| Host  | https://teamcity.jetbrains.com | optional  |
| Slug  |                                | optional  |
| Token |                                | required  |

Monitor a single build:

```
chroma-feedback --producer=teamcity

--teamcity-slug <project-id>
--teamcity-token <token>
```

Monitor multiple builds:

```
chroma-feedback --producer=teamcity

--teamcity-token <token>
```


Travis
------

| Name  | Default                   | Mandatory |
|-------|---------------------------|-----------|
| Host  | https://api.travis-ci.com | optional  |
| Slug  |                           | required  |
| Token |                           | required  |

Monitor a single build:

```
chroma-feedback --producer=travis

--travis-slug <username/repository>
--travis-token <token>
```

Monitor multiple builds:

```
chroma-feedback --producer=travis

--travis-slug <username>
--travis-token <token>
```


Wercker
-------

| Name  | Default                 | Mandatory |
|-------|-------------------------|-----------|
| Host  | https://app.wercker.com | optional  |
| Slug  |                         | required  |
| Token |                         | required  |

Monitor a single build:

```
chroma-feedback --producer=wercker

--wercker-slug <username/application>
--wercker-token <token>
```

Monitor multiple builds:

```
chroma-feedback --producer=wercker

--wercker-slug <username/application>
--wercker-slug <username/application>
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

| Name  | Mandatory |
|-------|-----------|
| Light | optional  |
| Group | optional  |

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


Luxafor Flag
------------

| Name   | Mandatory |
|--------|-----------|
| Device | optional  |

Indicate status via devices:

```
chroma-feedback --consumer=luxafor_flag

--luxafor-flag-device <device-name>
```


Magic Hue
---------

| Name | Mandatory |
|------|-----------|
| IP   | optional  |

Indicate status via lights:

```
chroma-feedback --consumer=magic_hue
```


Nanoleaf Light
--------------

| Name | Mandatory |
|------|-----------|
| IP   | optional  |

Indicate status via lights:

```
chroma-feedback --consumer=nanoleaf_light
```


Philips Hue
-----------

| Name  | Mandatory |
|-------|-----------|
| IP    | optional  |
| Light | optional  |
| Group | optional  |

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

--razer-chroma-device <device-name>
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


WiZ Light
---------

| Name | Mandatory |
|------|-----------|
| IP   | optional  |

Indicate status via lights:

```
chroma-feedback --consumer=wiz_light
```


Xiaomi Yeelight
---------------

| Name | Mandatory |
|------|-----------|
| IP   | optional  |

Indicate status via lights:

```
chroma-feedback --consumer=xiaomi_yeelight
```
