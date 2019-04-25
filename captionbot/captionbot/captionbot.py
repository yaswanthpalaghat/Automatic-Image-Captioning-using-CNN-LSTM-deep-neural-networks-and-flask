import json
import mimetypes
import os
import requests
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
import logging
logger = logging.getLogger("captionbot")


class CaptionBotException(Exception):
    pass


class CaptionBot:
    UPLOAD_URL = "https://www.captionbot.ai/api/upload"
    MESSAGES_URL = "https://captionbot.azurewebsites.net/api/messages"

    @staticmethod
    def _resp_error(resp):
        if not resp.ok:
            data = resp.json()
            msg = "HTTP error: {}".format(resp.status_code)
            if type(data) == dict and "Message" in data:
                msg += ", " + data.get("Message")
            raise CaptionBotException(msg)

    def __init__(self):
        self.session = requests.Session()

    def _upload(self, filename):
        url = self.UPLOAD_URL
        mime = mimetypes.guess_type(filename)[0]
        name = os.path.basename(filename)
        files = {'file': (name, open(filename, 'rb'), mime)}
        resp = self.session.post(url, files=files)
        logger.debug("upload: {}".format(resp))
        self._resp_error(resp)
        res = resp.text
        if res:
            return res[1:-1]

    def url_caption(self, image_url):
        data = {
            "Content": image_url,
            "Type": "CaptionRequest",
        }
        headers = {
            "Content-Type": "application/json; charset=utf-8"
        }
        url = self.MESSAGES_URL
        resp = self.session.post(url, data=json.dumps(data), headers=headers)
        logger.info("get_caption: {}".format(resp))
        if not resp.ok:
            return None
        res = resp.text[1:-1].replace('\\"', '"').replace('\\n', '\n')
        logger.info(res)
        return res

    def file_caption(self, filename):
        upload_filename = self._upload(filename)
        return self.url_caption(upload_filename)
