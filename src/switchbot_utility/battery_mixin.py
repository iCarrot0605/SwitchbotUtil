class BatteryMixin:
    """Switchbot battery mixin"""
    def get_battery(self):
        """Returns battery level"""
        status = self.get_status()
        return status["battery"]
