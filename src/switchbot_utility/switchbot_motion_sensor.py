from .switchbot_device import SwitchbotDevice


class SwitchbotMotionSensor(SwitchbotDevice):
    """Switchbot Motion Sensor class"""

    def __init__(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)

    def get_move_detected(self) -> str:
        """Returns if move detected"""
        status = self.get_status()
        return status["moveDetected"]

    def get_brightness(self) -> str:
        """Returns ambient brightness picked up by the sensor"""
        status = self.get_status()
        return status["brightness"]
