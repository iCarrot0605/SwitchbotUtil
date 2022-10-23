from switchbot.switchbot_meter import SwitchbotMeter
meter = SwitchbotMeter('meterDeviceId')
print(meter.get_temperature())