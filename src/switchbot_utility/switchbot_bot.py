from switchbot_utility.battery_mixin import BatteryMixin
from switchbot_utility.onoff_mixin import OnOffMixin
from switchbot_utility.switchbot_device import SwitchbotDevice


class SwitchbotBot(SwitchbotDevice, OnOffMixin, BatteryMixin):
    """Switchbot bot class"""

    def get_power(self) -> dict:
        """Returns ON/OFF state"""
        status = self.get_status()
        return status["power"]

    def press(self) -> str:
        """press action"""
        self._body["command"] = "press"
        result = self.command(self.deviceId, self._body)
        return result.text
