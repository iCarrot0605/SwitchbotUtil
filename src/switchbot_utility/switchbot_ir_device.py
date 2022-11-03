from .switchbot_device import SwitchbotDevice
from .onoff_ability import OnOffAbirity


class SwitchbotIrDevice(SwitchbotDevice, OnOffAbirity):
    """Switchbot virtual ir device"""
    def __init__(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)

