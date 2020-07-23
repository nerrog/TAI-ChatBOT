# TAI-ChatBOT

リクルートのA3RTというAPIの中のチャットボット作成のためのTalkAPIを使ってDiscordで会話するためのBOTです

## 必要ライブラリの準備
```
pip3 install discord
pip3 install pya3rt
```

## トークンの取得
いつもどうりDiscordDevelopersからBOTのトークンを生成する

[A3RT TalkAPI](https://a3rt.recruit-tech.co.jp/product/talkAPI/) からTalkAPIのトークンを取得する

## 実行
`python3 bot.py`

以上

# Demo
Discordサーバーに[こいつ](https://discord.com/api/oauth2/authorize?client_id=733265138362089492&permissions=2048&scope=bot)を招待してtai-chatというテキストチャンネルを作ってそこに話しかけると言葉を返します
※要閲覧・発言権限

# ライセンス
MITライセンス
