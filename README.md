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

Install the required OpenRazer driver:

* [Ubuntu / Linux Mint](https://openrazer.github.io/#ubuntu)
* [Debian](https://openrazer.github.io/#debian)
* [Arch Linux](https://openrazer.github.io/#arch)
* [Fedora](https://openrazer.github.io/#fedora)
* [openSUSE](https://openrazer.github.io/#opensuse)
* [Gentoo](https://openrazer.github.io/#gentoo)

Install Chroma Feedback using PyPI:

```
pip3 install chroma-feedback
```

Install Chroma Feedback using GitHub:

```
git clone https://github.com/redaxmedia/chroma-feedback.git
cd chroma-feedback
./setup.py install
```


Usage
-----

```
chroma-feedback [options]

-V, --version
-P, --provider <provider>
-H, --host <host>
-S, --slug <slug>
-A, --auth <auth>
-I, --background-interval <background-interval>
-B, --background-run
-D, --dry-run
-h, --help
```


AppVeyor
--------

| Name | Type   | Default                 | Mandatory | Support |
|------|--------|-------------------------|-----------|---------|
| Host | string | https://ci.appveyor.com | optional  | ✔       |
| Slug | string |                         | optional  | ✔       |
| Auth | string |                         | optional  | ✔       |

Monitor a single project by slug:

```
chroma-feedback --provider=appveyor --slug=redaxmedia/chroma-feedback
```

Monitor multiple projects by auth:

```
chroma-feedback --provider=appveyor --auth={TOKEN}
```


Circle
------

| Name | Type   | Default              | Mandatory | Support |
|------|--------|----------------------|-----------|---------|
| Host | string | https://circleci.com | optional  | ✔       |
| Slug | string |                      | optional  | ✔       |
| Auth | string |                      | optional  | ✔       |

Monitor a single project by slug:

```
chroma-feedback --provider=circle --slug=github/redaxmedia/chroma-feedback
```

Monitor multiple projects by auth:

```
chroma-feedback --provider=circle --auth={TOKEN}
```


GitHub
------

| Name | Type   | Default                | Mandatory | Support |
|------|--------|------------------------|-----------|---------|
| Host | string | https://api.github.com | optional  | ✔       |
| Slug | string |                        | required  | ✔       |
| Auth | string |                        | required  | ✔       |

Monitor a single project by slug and auth:

```
chroma-feedback --provider=github --slug=redaxmedia/chroma-feedback --auth={USERNAME:PASSWORD}
```

Monitor multiple projects by slug and auth:

```
chroma-feedback --provider=github --slug={SLUG} --slug={SLUG} --auth={USERNAME:PASSWORD}
```


GitLab
------

| Name | Type   | Default            | Mandatory | Support |
|------|--------|--------------------|-----------|---------|
| Host | string | https://gitlab.com | optional  | ✔       |
| Slug | string |                    | required  | ✔       |
| Auth | string |                    | required  | ✔       |

Monitor a single project by slug and auth:

```
chroma-feedback --provider=gitlab --slug={SLUG} --auth={TOKEN}
```

Monitor multiple projects by slug and auth:

```
chroma-feedback --provider=gitlab --slug={SLUG} --slug={SLUG} --auth={TOKEN}
```


Jenkins
-------

| Name | Type   | Default | Mandatory | Support |
|------|--------|---------|-----------|---------|
| Host | string |         | required  | ✔       |
| Slug | string |         | required  | ✔       |
| Auth | string |         |           | ✖       |

Monitor a single project by slug:

```
chroma-feedback --provider=jenkins --host={HOST} --slug={SLUG}
```

Monitor multiple projects by slug:

```
chroma-feedback --provider=jenkins --host={HOST} --slug={SLUG} --slug={SLUG}
```


TeamCity
--------

| Name | Type   | Default                        | Mandatory | Support |
|------|--------|--------------------------------|-----------|---------|
| Host | string | https://teamcity.jetbrains.com | optional  | ✔       |
| Slug | string |                                | required  | ✔       |
| Auth | string |                                | required  | ✔       |

Monitor a single project by slug and auth:

```
chroma-feedback --provider=teamcity --slug={SLUG} --auth={USERNAME:PASSWORD}
```

Monitor multiple projects by auth:

```
chroma-feedback --provider=teamcity --auth={USERNAME:PASSWORD}
```


Travis
------

| Name | Type   | Default                   | Mandatory | Support |
|------|--------|---------------------------|-----------|---------|
| Host | string | https://api.travis-ci.org | optional  | ✔       |
| Slug | string |                           | required  | ✔       |
| Auth | string |                           |           | ✖       |

Monitor a single project by slug:

```
chroma-feedback --provider=travis --slug=redaxmedia/chroma-feedback
```

Monitor multiple projects by slug:

```
chroma-feedback --provider=travis --slug=redaxmedia
```


Errors
------

| Message                  | Type        | Description                                     |
|--------------------------|-------------|-------------------------------------------------|
| Python x.x not supported | System      | Unsupported Python version is called            |
| Driver not found         | ImportError | Module `openrazer.client` could not be imported |
| Daemon not found         | Exception   | The `DeviceManager` throwed a `DaemonNotFound`  |
| Device not found         | General     | There is no supported device connected          |
| Data not found           | General     | There is no data available for your request     |


Indicators
----------

| Status  | Color  | Effect  |
|---------|--------|---------|
| Passed  | Green  | Static  |
| Process | Yellow | Static  |
| Errored | White  | Pulsate |
| Failed  | Red    | Pulsate |
