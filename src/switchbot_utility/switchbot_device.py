import json
import sys

import requests

from .switchbot import Switchbot
from .command_mixin import CommandMixin


class SwitchbotDevice(Switchbot, CommandMixin):
    """Switchbot device class"""

    _body = {"commandType": "command", "parameter": "default"}
    _baseurl = "https://api.switch-bot.com/v1.1/devices/"

    def __init__(self, deviceId):
        """Constructor"""
        self.deviceId = deviceId

    def get_status(self) -> dict:
        """Get device information"""
        header = self.gen_sign()
        response = requests.get(
            self._baseurl + self.deviceId + "/status",
            headers=header,
        )
        status = json.loads(response.text)
        if status["message"] != "success":
            sys.exit(status["message"])
        else:
            return status["body"]

