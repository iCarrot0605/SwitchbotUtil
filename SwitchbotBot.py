from SwitchbotDevice import SwitchbotDevice

class SwitchbotBot(SwitchbotDevice):
    """Switchbot bot class"""
    def __init__(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)

    def get_power(self):
        """Returns device power status"""
        status = self.get_status()
        return status['power']

    def press(self):
        """press action"""
        body = {
            "commandType": "command",
            "parameter": "default",
            "command": "press"
        }
        result = self.command(self.deviceId, body)
        return result.text
