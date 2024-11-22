from switchbot_utility.battery_mixin import BatteryMixin
from switchbot_utility.switchbot_device import SwitchbotDevice


class SwitchbotMeter(SwitchbotDevice, BatteryMixin):
    """Switchbot meter class"""

    def get_temperature(self) -> str:
        """Returns temperature from meter"""
        status = self.get_status()
        return status["temperature"]

    def get_humidity(self) -> str:
        """Returns humidity from meter"""
        status = self.get_status()
        return status["humidity"]
