from .switchbot_device import SwitchbotDevice
from .onoff_ability import OnOffAbility


class SwitchbotBot(SwitchbotDevice, OnOffAbility):
    """Switchbot bot class"""

    def __init__(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)

    def get_power(self):
        """Returns ON/OFF state"""
        status = self.get_status()
        return status["power"]

    def press(self):
        """press action"""
        self._body["command"] = "press"
        result = self.command(self.deviceId, self._body)
        return result.text
