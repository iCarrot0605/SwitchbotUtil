from switchbot_utility.switchbot_device import SwitchbotDevice


class SwitchbotHub2(SwitchbotDevice):
    """Switchbot Hub2 class"""

    def get_temperature(self) -> str:
        """Returns temperature from Hub2"""
        status = self.get_status()
        return status["temperature"]

    def get_humidity(self) -> str:
        """Returns humidity from Hub2"""
        status = self.get_status()
        return status["humidity"]

    def get_light_level(self) -> int:
        """Returns the level of illuminance of the ambience light, 1~20"""
        status = self.get_status()
        return status["lightLevel"]
