Chroma Feedback
===============

> Turn your Razer keyboard, mouse or headphone into a extreme feedback device for Travis CI.

[![Build Status](https://img.shields.io/travis/redaxmedia/chroma-feedback.svg)](https://travis-ci.org/redaxmedia/chroma-feedback)


Installation
------------

Install the OpenRazer driver:

* [Ubuntu / Linux Mint](https://openrazer.github.io/#ubuntu)
* [Debian](https://openrazer.github.io/#debian)
* [Arch Linux](https://openrazer.github.io/#arch)
* [Fedora](https://openrazer.github.io/#fedora)
* [openSUSE](https://openrazer.github.io/#opensuse)
* [Gentoo](https://openrazer.github.io/#gentoo)

Install the Chroma Feedback with PyPI:

```
pip install chroma-feedback
```

Build and install the Chroma Feedback using the `setup.py` file:

```
./setup.py build
```

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

Validate each repositories of `redaxmedia` every minute:

```
chroma-feedback redaxmedia 60
```

Validate the `chroma-feedback` repository of `redaxmedia` one time:

```
chroma-feedback redaxmedia/chroma-feedback
```
