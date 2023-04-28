import json

import requests


class CommandMixin:
    _body = {"commandType": "command", "parameter": "default"}
    _baseurl = "https://api.switch-bot.com/v1.1/devices/"

    def command(self, deviceId: str, body: dict):
        """Send command"""

        header = self.gen_sign()
        return requests.post(
            self._baseurl + deviceId + "/commands",
            headers=header,
            data=json.dumps(body),
        )
