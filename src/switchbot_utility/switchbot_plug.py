from switchbot_utility.onoff_mixin import OnOffMixin
from switchbot_utility.switchbot_device import SwitchbotDevice


class SwitchbotPlug(SwitchbotDevice, OnOffMixin):
    """Switchbot Plug class"""

    def get_power(self) -> str:
        """Returns device power status"""
        status = self.get_status()
        return status["power"]
