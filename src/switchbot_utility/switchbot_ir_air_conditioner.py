from .switchbot_ir_device import SwitchbotIrDevice


class IrAirConditioner(SwitchbotIrDevice):
    """Switchbot virtual ir Air Conditioner"""

    def __init__(self, deviceId):
        super().__init__(deviceId)

    def set_all(
        self, temperature: int, mode: int, fan_speed: int, power_state: str
    ) -> str:
        """Set the unit of temperature is in celsius

        args:
            temperature: temperature in celsius
            mode: 1(auto), 2(cool), 3(dry), 4(fan), 5(heat)
            fan_speed: 1(auto), 2(low), 3(medium), 4(high)
            power_state: 'on' or 'off' (must be quoted)

        e.g. set_all(26,1, 3, 'on')"""
        self._body["command"] = "setAll"
        parameter = f"{temperature}, {mode}, {fan_speed}, {power_state}"
        self._body["parameter"] = parameter

        result = self.command(self.deviceId, self._body)
        return result.text
