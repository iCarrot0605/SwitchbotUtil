from .switchbot_ceiling_light import SwitchbotCeilingLight


class SwithbotCeilingLightPro(SwitchbotCeilingLight):
    """Switchbot Ceiling Light class"""

    def __init__(self, deviceId):
        """Constructor"""
        super().__init__(deviceId)
