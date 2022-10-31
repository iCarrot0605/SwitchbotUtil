from .switchbot import Switchbot
import requests
import json

class SwitchbotDevice(Switchbot):
    """Switchbot device class"""
    def __init__(self, deviceId):
        """Constructor"""
        self.deviceId = deviceId

    def get_status(self):
        """Get device information"""
        header = self.gen_sign()
        response = requests.get("https://api.switch-bot.com/v1.1/devices/" + self.deviceId + "/status", headers=header)
        status   = json.loads(response.text)
        return status['body']

    def command(self, deviceId, body):
        """Send command"""
        header = self.gen_sign()
        return requests.post("https://api.switch-bot.com/v1.1/devices/" + deviceId + "/commands", headers=header, data=json.dumps(body))

    def turn_off(self):
        """Turn off device"""
        body = {
            "commandType": "command",
            "parameter": "default",
            "command": "turnOff"
        }
        result = self.command(self.deviceId, body)
        return result.text

    def turn_on(self):
        """Turn on device"""
        body = {
            "commandType": "command",
            "parameter": "default",
            "command": "turnOn"
        }
        result = self.command(self.deviceId, body)
        return result.text
