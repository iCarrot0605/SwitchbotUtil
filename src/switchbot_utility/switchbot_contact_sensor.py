from .switchbot_motion_sensor import SwitchbotMotionSensor


class SwitchbotContactSensor(SwitchbotMotionSensor):
    """Switchbot Contact Sensor class"""

    def __init__(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)

    def get_open_state(self):
        """Returns the open state of the sensor"""
        status = self.get_status()
        return status["openState"]
