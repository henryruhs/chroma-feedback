Chroma Feedback
===============

> Turn your Razer keyboard, mouse or headphone into a extreme feedback device.

[![Build Status](https://img.shields.io/travis/redaxmedia/chroma-feedback.svg)](https://travis-ci.org/redaxmedia/chroma-feedback)
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
-P, --provider <provider>
-S, --slug <slug>
-I, --background-interval <background-interval>
-B, --background-run
-D, --dry-run
-h, --help
```


Examples
--------

Monitor the `redaxscript` repository of `redaxmedia` on `AppVeyor` one time:

```
chroma-feedback --provider=appveyor --slug=redaxmedia/redaxscript
```

Monitor the `redaxscript` repository of `redaxscript` on `Circle` one time:

```
chroma-feedback --provider=circle --slug=github/redaxscript/redaxscript
```

Monitor the `redaxscript` on `Jenkins` one time:

```
chroma-feedback --provider=jenkins --host=http://localhost:8080 --slug=redaxscript
```

Monitor each repositories of `redaxmedia` and `redaxscript` on `Travis` one time:

```
chroma-feedback --provider=travis --slug=redaxmedia --slug=redaxscript
```

Monitor each repositories of `redaxmedia` on `Travis` every minute:

```
chroma-feedback --provider=travis --slug=redaxmedia --background-run --background-interval=60
```


Providers
---------

| Name     | Value    |
|----------|----------|
| AppVeyor | appveyor | 
| Circle   | circle   |
| Jenkins  | jenkins  |
| Travis   | travis   |


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
