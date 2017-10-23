Razer Chroma Feedback
=====================

> Continuous Integration feedback for Razer Chroma devices.

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

Clone the repository:

```
git clone https://github.com/redaxmedia/razer-chroma-feedback.git
cd razer-chroma-feedback
```


Usage
-----

```
./feedback.py [repository] [interval]
```


Examples
--------

Validate each repositories of `redaxmedia` every minute:

```
./feedback redaxmedia 60
```

Validate the `razer-chroma-feedback` repository of `redaxmedia` one time:

```
./feedback redaxmedia/razer-chroma-feedback
```
