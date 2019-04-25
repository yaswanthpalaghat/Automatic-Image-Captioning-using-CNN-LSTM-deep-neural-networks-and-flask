# captionbot

[![PyPi Package Version](https://img.shields.io/pypi/v/captionbot.svg)](https://pypi.python.org/pypi/captionbot)

Captionbot is a simple API wrapper for https://www.captionbot.ai/

## Installation

You can install captionbot using pip:
```bash
$ pip install captionbot
```
## Usage

To use, simply do:
    
```python
>>> from captionbot import CaptionBot
>>> c = CaptionBot()
>>> c.url_caption('your image url here')
>>> c.file_caption('your local image filename here')
```
