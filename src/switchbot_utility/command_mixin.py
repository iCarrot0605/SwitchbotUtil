import json
import sys

import requests
from requests.exceptions import Timeout


class CommandMixin:
    _body = {"commandType": "command", "parameter": "default"}
    _baseurl = "https://api.switch-bot.com/v1.1/devices/"

    def command(self, deviceId: str, body: dict):
        """Send command"""

        header = self.gen_sign()
        try:
            return requests.post(
                self._baseurl + deviceId + "/commands",
                headers=header,
                data=json.dumps(body),
                timeout=(3.0, 7.5)
            )
        except Timeout:
            sys.exit("Timeout")
