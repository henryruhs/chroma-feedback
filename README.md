Chroma Feedback
===============

> Turn your Razer keyboard, mouse or headphone into a extreme feedback device for Travis CI.

[![Build Status](https://img.shields.io/travis/redaxmedia/chroma-feedback.svg)](https://travis-ci.org/redaxmedia/chroma-feedback)
[![PyPI](https://img.shields.io/pypi/v/chroma-feedback.svg)](https://pypi.org/project/chroma-feedback)
[![License](https://img.shields.io/pypi/l/chroma-feedback.svg)](https://pypi.org/project/chroma-feedback)


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
git clone https://github.com/redaxmedia/chroma-feedback.git
cd chroma-feedback
./setup.py install
```


Usage
-----

```
chroma-feedback [options]

-V, --version
-S, --slug <slug>
-I, --background-interval <background-interval>
-B, --background-run
-D, --dry-run
-h, --help
```


Examples
--------

Monitor each repositories of `redaxmedia` every minute:

```
chroma-feedback --slug=redaxmedia --background-run --background-interval=60
```

Monitor each repositories of `redaxmedia` and `redaxscript` one time:

```
chroma-feedback --slug=redaxmedia --slug=redaxscript
```

Monitor the `chroma-feedback` repository of `redaxmedia` one time:

```
chroma-feedback --slug=redaxmedia/chroma-feedback
```


Errors
------

| Message          | Type        | Description                                     |
|------------------|-------------|-------------------------------------------------|
| Driver not found | ImportError | Module `openrazer.client` could not be imported |
| Daemon not found | Exception   | The `DeviceManager` throwed a `DaemonNotFound`  |
| Device not found | General     | There is no supported device connected          |
| Data not found   | General     | There is no data available for your request     |


Indicators
----------

| Status  | Color  | Effect  |
|---------|--------|---------|
| Process | Yellow | Static  |
| Passed  | Green  | Static  |
| Errored | White  | Pulsate |
| Failed  | Red    | Pulsate |
