from .switchbot_device import SwitchbotDevice
from .onoff_ability import OnOffAbility


class SwitchbotIrDevice(SwitchbotDevice, OnOffAbility):
    """Switchbot virtual ir device"""

    def __init__(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)
