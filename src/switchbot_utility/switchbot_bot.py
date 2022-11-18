from .onoff_device import OnOffDevice


class SwitchbotBot(OnOffDevice):
    """Switchbot bot class"""

    def __init__(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)

    def get_power(self) -> dict:
        """Returns ON/OFF state"""
        status = self.get_status()
        return status["power"]

    def press(self) -> str:
        """press action"""
        self._body["command"] = "press"
        result = self.command(self.deviceId, self._body)
        return result.text
