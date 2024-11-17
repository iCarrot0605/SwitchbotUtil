import json

import requests

from switchbot_utility.switchbot import Switchbot


class SwitchbotWebhook(Switchbot):
    _baseurl = "https://api.switch-bot.com/v1.1/webhook/"

    def __init__(self):
        super().__init__()

    """Switchbot Webhook action"""

    def http_request(self, url: str, headers: dict, data: dict):
        return requests.post(
            url, headers, data,
        )

    def setup_webhook(self, url: str) -> str:
        """Setup Webhook"""
        header = self.gen_sign()
        body = {"action": "setupWebhook", "deviceList": "ALL"}
        body["url"] = url
        posturl = self._baseurl + "setupWebhook"
        response = http_request(
            posturl, headers=header, data=json.dumps(body)
        )
        return response.text

    def query_url(self) -> str:
        """Get webhook configuration"""
        header = self.gen_sign()
        body = {"action": "queryUrl"}
        posturl = self._baseurl + "queryWebhook"
        response = http_request(
            posturl, headers=header, data=json.dumps(body)
        )
        return response.text

    def query_details(self, url: str) -> str:
        """Get webhook detail configurations"""
        header = self.gen_sign()
        body = {"action": "queryDetails"}
        body["urls"] = url
        posturl = self._baseurl + "queryWebhook"
        response = http_request(
            posturl, headers=header, data=json.dumps(body)
        )
        return response.text

    def update_webhook(self, url: str, enable: bool) -> str:
        """Update webhook url"""
        header = self.gen_sign()
        body = {}
        body["action"] = "updateWebhook"
        body["config"] = {"url": {}, "enable": {}}
        body["config"]["url"] = url
        body["config"]["enable"] = enable
        posturl = self._baseurl + "updateWebhook"
        response = http_request(
            posturl, headers=header, data=json.dumps(body)
        )
        return response.text

    def delete_webhook(self, url: str) -> str:
        """Delete webhook"""
        header = self.gen_sign()
        body = {"action": "deleteWebhook"}
        body["url"] = url
        posturl = self._baseurl + "deleteWebhook"
        response = http_request(
            posturl, headers=header, data=json.dumps(body)
        )
        return response.text
