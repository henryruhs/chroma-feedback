Chroma Feedback
===============

> Turn your RGB powered hardware into a status indicator for continuous integration, continuous deployment and infrastructure monitoring.

[![Build Status](https://img.shields.io/github/workflow/status/henryruhs/chroma-feedback/ci.svg)](https://github.com/henryruhs/chroma-feedback/actions?query=workflow:ci)
[![Coverage Status](https://img.shields.io/coveralls/henryruhs/chroma-feedback.svg)](https://coveralls.io/r/henryruhs/chroma-feedback)
[![PyPI](https://img.shields.io/pypi/v/chroma-feedback.svg)](https://pypi.org/project/chroma-feedback)
[![License](https://img.shields.io/pypi/l/chroma-feedback.svg)](https://pypi.org/project/chroma-feedback)


Preview
-------

![Terminal Session](https://raw.githubusercontent.com/henryruhs/chroma-feedback/master/.github/terminal-session.svg?sanitize=true)


Installation
------------

Install Chroma Feedback:

```
pip3 install chroma-feedback
```

Install the dependencies for Linux:

```
apt-get install libudev-dev libusb-1.0-0-dev libhidapi-libusb0
```

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
-L, --log-level
-h, --help
```


Documentation
-------------

Read the [documenation](https://henryruhs.gitbook.io/chroma-feedback) for a deep dive.
