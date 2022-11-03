from .switchbot_device import SwitchbotDevice
from .onoff_ability import OnOffAbirity


class SwitchbotBot(SwitchbotDevice, OnOffAbirity):
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
        self._body['command'] = "press"
        result = self.command(self.deviceId, self._body)
        return result.text
