Razer Chroma Feedback
=====================

> Continuous Integration feedback for Razer Chroma devices.

[![Build Status](https://img.shields.io/travis/redaxmedia/razer-chroma-feedback.svg)](https://travis-ci.org/redaxmedia/razer-chroma-feedback)


Installation
------------

Install the Open Razer driver:

```
add-apt-repository ppa:openrazer/stable
apt update
apt install openrazer-meta
```

Clone the repository:

```
git clone https://github.com/redaxmedia/razer-chroma-feedback.git
cd razer-chroma-feedback
```


Usage
-----

Pass your Travis CI owner and repository:

```
bin/feedback.py :owner/:repository
```


Examples
--------

```
bin/feedback redaxmedia/razer-chroma-feedback
```
