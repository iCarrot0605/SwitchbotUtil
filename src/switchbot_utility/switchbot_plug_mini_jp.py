from .switchbot_plug_mini_us import SwitchbotPlugMiniUS


class SwitchbotPlugMiniJP(SwitchbotPlugMiniUS):
    """Switchbot Plug Mini(US) class"""

    def __init__(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)
