# Switchbot_utility

Python Switchbot Utilities using Switchbot API.

## Getting start

Install from PyPI

```python
pip install switchbot_utility
```

Get token and secret,

1. Download the SwitchBot app on App Store or Google Play Store
2. Register a SwitchBot account and log in into your account
3. Generate an Open Token within the app
a) Go to Profile > Preference
b) Tap App Version 10 times. Developer Options will show up
c) Tap Developer Options
d) Copy token and secret

create `settings.json` file, and fill token and secret.

```python
{
    "token": "",
    "secret": ""
}
```

Run example script.

```python
python3 example/get_devicelist.py
```

Scripts makes `deviceList.txt`.You can manipulate device using diviceId.
