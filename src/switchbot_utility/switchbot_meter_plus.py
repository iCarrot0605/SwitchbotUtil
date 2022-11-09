from .switchbot_meter import SwitchbotMeter


class SwitchbotMeterPlus(SwitchbotMeter):
    """Switchbot Meter Plus class"""

    def __init__(self, deviceId):
        super().__init__(deviceId)
