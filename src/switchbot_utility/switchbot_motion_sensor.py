from switchbot_utility.battery_mixin import BatteryMixin
from switchbot_utility.switchbot_device import SwitchbotDevice


class SwitchbotMotionSensor(SwitchbotDevice, BatteryMixin):
    """Switchbot Motion Sensor class"""

    def get_move_detected(self) -> str:
        """Returns if move detected"""
        status = self.get_status()
        return status["moveDetected"]

    def get_brightness(self) -> str:
        """Returns ambient brightness picked up by the sensor"""
        status = self.get_status()
        return status["brightness"]
