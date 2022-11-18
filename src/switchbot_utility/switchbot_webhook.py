import json

import requests

from .switchbot import Switchbot


class SwitchbotWebhook(Switchbot):
    _baseurl = "https://api.switch-bot.com/v1.1/webhook/"

    def __init__(self):
        super().__init__()

    """Switchbot Webhook action"""

    def setup_webhook(self, url: str) -> str:
        """Setup Webhook"""
        header = self.gen_sign()
        body = {"action": "setupWebhook", "deviceList": "ALL"}
        body["url"] = url
        posturl = self._baseurl + "setupWebhook"
        response = requests.post(
            posturl, headers=header, data=json.dumps(body)
        )
        return response.text

    def query_url(self) -> str:
        """Get webhook configuration"""
        header = self.gen_sign()
        body = {"action": "queryUrl"}
        posturl = self._baseurl + "queryWebhook"
        response = requests.post(
            posturl, headers=header, data=json.dumps(body)
        )
        return response.text

    def query_details(self, url: str) -> str:
        """Get webhook detail configurations"""
        header = self.gen_sign()
        body = {"action": "queryDetails"}
        body["urls"] = url
        posturl = self._baseurl + "queryWebhook"
        response = requests.post(
            posturl, headers=header, data=json.dumps(body)
        )
        return response.text

    def update_webhook(self, url: str) -> str:
        """Update webhook url"""
        header = self.gen_sign()
        body = {"action": "updateWebhook"}
        body["urls"] = url
        posturl = self._baseurl + "queryWebhook"
        response = requests.post(
            posturl, headers=header, data=json.dumps(body)
        )
        return response.text

    def delete_webhook(self, url: str) -> str:
        """Delete webhook"""
        header = self.gen_sign()
        body = {"action": "deleteWebhook"}
        body["url"] = url
        posturl = self._baseurl + "deleteWebhook"
        response = requests.post(
            posturl, headers=header, data=json.dumps(body)
        )
        return response.text
