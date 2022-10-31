import requests
import json
from .switchbot import Switchbot


class SwitchbotWebhook(Switchbot):
    baseurl = 'https://api.switch-bot.com/v1.1/webhook/'

    def __init__(self):
        super().__init__()

    """Switchbot Webhook action"""
    def setup_webhook(self, url):
        """Setup Webhook"""
        header = self.gen_sign()
        body = {"action": "setupWebhook",
                "deviceList": "ALL"}
        body['url'] = url
        posturl = self.baseurl + 'setupWebhook'
        response = requests.post(posturl, headers=header, data=json.dumps(body))
        return response.text

    def query_url(self):
        """Get webhook configuration"""
        header = self.gen_sign()
        body = {"action": "queryUrl"}
        posturl = self.baseurl + 'queryWebhook'
        response = requests.post(posturl, headers=header, data=json.dumps(body))
        return response.text
    
    def query_details(self, url):
        """Get webhook detail configurations"""
        header = self.gen_sign()
        body = {"action": "queryDetails"}
        body['urls'] = url
        posturl = self.baseurl + 'queryWebhook'
        response = requests.post(posturl, headers=header,
                                 data=json.dumps(body))
        return response.text

    def update_webhook(self, url):
        """Update webhook url"""
        header = self.gen_sign()
        body = {"action": "updateWebhook"}
        body['urls'] = url
        posturl = self.baseurl + 'queryWebhook'
        response = requests.post(posturl, headers=header, data=json.dumps(body))
        return response.text
    
    def delete_webhook(self, url):
        """Delete webhook"""
        header = self.gen_sign()
        body = {"action": "deleteWebhook"}
        body['url'] = url
        posturl = self.baseurl + 'deleteWebhook'
        response = requests.post(posturl, headers=header, data=json.dumps(body))
        return response.text
