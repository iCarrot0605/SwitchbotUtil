from switchbot_utility.switchbot_meter import SwitchbotMeter


class SwitchbotMeterProCO2(SwitchbotMeter):
    """Switchbot Meter Pro(CO2) class"""

    def get_co2(self) -> str:
        """Returns CO2 ppm value 0-9999 from meter"""
        status = self.get_status()
        return status["CO2"]
