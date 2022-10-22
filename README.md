# SwitchbotUtil

Switchbot Utilities

## 使い方

1. tokenとsecretの入手
    1. Switchbot App(V6.14以降)をダウンロード
    1. 「プロフィール」＞「設定」へと進み、「アプリバージョン」のフィールドを10回タップすると表示される「開発者向けオプション」から取得することができます。
1. settings.jsonファイルにtokenとsecretを記入
1. `python3 Switchbot.py`で同じディレクトリ内にdeviceList.txtというSwitchbotデバイス一覧ファイルが作成されます

## サンプルプログラム

Switchbot Botの電源ON/OFFを確認する。

```python
from SwitchbotBot import SwitchbotBot
bot = SwitchbotBot('YourdeviceId')
print(bot.get_power())
```

## TODO

Switchbot Keypad/Keypad touchのパスコード作成は今のところちゃんと動作していません。原因不明です。
