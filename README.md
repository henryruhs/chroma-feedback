Chroma Feedback
===============

> Turn your Razer keyboard, mouse or headphone into a extreme feedback device for Travis CI.

[![Build Status](https://img.shields.io/travis/redaxmedia/razer-chroma-feedback.svg)](https://travis-ci.org/redaxmedia/razer-chroma-feedback)


Installation
------------

Install the Open Razer driver:

* [Ubuntu / Linux Mint](https://openrazer.github.io/#ubuntu)
* [Debian](https://openrazer.github.io/#debian)
* [Arch Linux](https://openrazer.github.io/#arch)
* [Fedora](https://openrazer.github.io/#fedora)
* [openSUSE](https://openrazer.github.io/#opensuse)
* [Gentoo](https://openrazer.github.io/#gentoo)

Install the Razer Chroma Feedback:

```
pip install razer-chroma-feedback
```


Usage
-----

```
razer-chroma-feedback [repository] [interval]
```


Examples
--------

Validate each repositories of `redaxmedia` every minute:

```
razer-chroma-feedback redaxmedia 60
```

Validate the `razer-chroma-feedback` repository of `redaxmedia` one time:

```
razer-chroma-feedback redaxmedia/razer-chroma-feedback
```
