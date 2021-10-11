# README

## Description

- 日本のTwitterのトレンド1～50位に任意の文字列が含まれる場合、コンソールとデスクトップへ通知を行うアプリケーションです。障害チェックなどに。

![thumb](https://user-images.githubusercontent.com/41136135/136813788-460f24eb-3a57-4224-a166-2c067d04d19a.png)

## Getting Started

### Clone

```bash
git clone git@github.com:kiyotd/app-twitter-trend-alert.git
```

### Configuring the Twitter API

Rename the `.env.example` file to `.env` file.  
Set your Twitter API keys and tokens.


### Building an Environment

```bash
cd app-twitter-trend-alert
python3 -m venv venv
source ./venv/bin/activate.fish # for fish
(venv) pip install tweepy
(venv) pip install python-dotenv
(venv) pip install plyer
(venv) pip install git+https://github.com/kivy/pyobjus/
```

### Keyword Specifications

edit `main.py`

```
words = ["GitHub", "AWS", "Slack", "Gmail", "障害"]
```

### Run the app

```bash
(venv) python main.py
```

## Licence

The MIT License

## Author

**kiyotd**  
web designer, front-end engineer

- [kiyotd.com](https://kiyotd.com/)
- [twitter](https://twitter.com/_kiyotd)
- [github](https://github.com/kiyotd)
