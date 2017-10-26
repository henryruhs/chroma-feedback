Chroma Feedback
===============

> Turn your Razer keyboard, mouse or headphone into a extreme feedback device for Travis CI.

[![Build Status](https://img.shields.io/travis/redaxmedia/chroma-feedback.svg)](https://travis-ci.org/redaxmedia/chroma-feedback)
[![PyPI](https://img.shields.io/pypi/v/chroma-feedback.svg)](https://pypi.org/project/chroma-feedback)


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
pip install chroma-feedback
```

Install Chroma Feedback using the `setup.py` file:

```
./setup.py install
```


Usage
-----

```
chroma-feedback [repository] [interval]
```


Examples
--------

Monitor each repositories of `redaxmedia` every minute:

```
chroma-feedback redaxmedia 60
```

Monitor the `chroma-feedback` repository of `redaxmedia` one time:

```
chroma-feedback redaxmedia/chroma-feedback
```
