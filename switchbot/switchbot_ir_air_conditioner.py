from .switchbot_ir_device import SwitchbotIrDevice


class IrAirConditioner(SwitchbotIrDevice):
    """Switchbot virtual ir Air Conditioner"""
    def __init__(self, deviceId):
        super().__init__(deviceId)

    def set_all(self, temperature, mode, fan_speed, power_state):
        """Set the unit of temperature is in celsius"""
        self._body['command'] = "setAll"
        parameter = f'{temperature}, {mode}, {fan_speed}, {power_state}'
        self._body['parameter'] = parameter

        result = self.command(self.deviceId, self._body)
        return result.text
