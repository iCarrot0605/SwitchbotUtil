from .switchbot_device import SwitchbotDevice


class SwitchbotIrDevice(SwitchbotDevice):
    """Switchbot virtual ir device"""
    def __init__(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)

