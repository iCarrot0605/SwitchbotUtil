from .onoff_device import OnOffDevice


class SwitchbotPlug(OnOffDevice):
    """Switchbot Plug class"""

    def __init__(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)

    def get_power(self) -> str:
        """Returns device power status"""
        status = self.get_status()
        return status["power"]
