import switchbot_utility as sbu

plug = sbu.SwitchbotPlug("PlugDeviceId")
print(plug.get_power())
