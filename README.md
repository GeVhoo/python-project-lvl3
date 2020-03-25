# Page Loader
[![Maintainability](https://api.codeclimate.com/v1/badges/db765234278ad05eaddd/maintainability)](https://codeclimate.com/github/GeVhoo/python-project-lvl3/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/db765234278ad05eaddd/test_coverage)](https://codeclimate.com/github/GeVhoo/python-project-lvl3/test_coverage)
[![Build Status](https://travis-ci.org/GeVhoo/python-project-lvl3.svg?branch=master)](https://travis-ci.org/GeVhoo/python-project-lvl3)

Hello World!

This is my third project that i do in Hexlet course.
It is a useful utility to download addresses from the network.

Functions:
* You can specify the folder in which you want to download the finished file. To select the output format, you must specify the key. For example:
```bash
gv-page-loader https://ru.hexlet.io/courses -o /tmp/tests
```
* You can choose the logging level: 'info' or 'debug'. Default level 'info'.
```bash
gv-page-loader https://ru.hexlet.io/courses -o /tmp/tests -l debug
```
* The utility downloads all resources on the page and changes the page so that it starts to link to local versions.

Hope you enjoy it!
##

### Direct install:

```bash
pip install -i https://test.pypi.org/simple/ gevhoo-page-loader --extra-index-url https://pypi.org/simple/ --user
```

[![asciicast](https://asciinema.org/a/f2tp7U0xKu2imZNFi5HvTUZA9.svg)](https://asciinema.org/a/f2tp7U0xKu2imZNFi5HvTUZA9)

### Using

[![asciicast](https://asciinema.org/a/ZB2lRDtr0hVNGlmWShc7cbVz1.svg)](https://asciinema.org/a/ZB2lRDtr0hVNGlmWShc7cbVz1)

### Using with debug logging level

[![asciicast](https://asciinema.org/a/MmJfJZUiSCGBTEaxJazttDXdV.svg)](https://asciinema.org/a/MmJfJZUiSCGBTEaxJazttDXdV)

### Links

This project was built using these tools:

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://poetry.eustace.io/)                                        | "Python dependency management and packaging made easy"  |
| [Flake8](https://flake8.pycqa.org/)                                         | "Linter"                                                |
| [CodeClimate](https://codeclimate.com/)                                     | "Verifying code quality in automatic mode"              |
| [Travis-ci](https://travis-ci.org/)                                         | "Continuous Integration"                                |
| [pytest](https://pypi.org/project/pytest/)                                  | "For test coverage"                                     |

