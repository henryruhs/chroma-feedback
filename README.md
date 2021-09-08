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
pip3 install chroma-feedback
```

Install the dependencies for Linux:

```
apt-get install libusb-1.0-0-dev libudev-dev
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
-h, --help
```


Documentation
-------------

Read the [documenation](https://redaxmedia.gitbook.io/chroma-feedback) for a deep dive.
