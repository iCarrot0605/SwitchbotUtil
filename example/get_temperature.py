import switchbot_utility as sbu

meter = sbu.SwitchbotMeter("meterDeviceId")
print(meter.get_temperature())
