# README

## Description

- 日本のTwitterのトレンド1～50位に任意の文字列が含まれる場合、コンソールとデスクトップへ通知を行うアプリケーションです。障害チェックなどに。

![thumb](https://user-images.githubusercontent.com/41136135/100298851-83c1fc80-2fd5-11eb-8807-bc20b2658f9c.png)

## Getting Started

### Clone

```bash
git clone https://github.com/kiyotd/app-twitter-trend-alert.git
```

### Configuring the Twitter API

Rename the `.env.example` file to `.env` file.  
Set your Twitter API keys and tokens.


### Building an Environment

```bash
cd app-twitter-trend-alert
pipenv install
```

### Keyword Specifications

edit `main.py`

```
words = ["GitHub", "AWS", "Slack", "Gmail", "障害"]
```

### Run the app

```bash
pipenv run python main.py
```

## Licence

The MIT License

## Author

**kiyotd**  
web designer, front-end engineer

- [kiyotd.com](https://kiyotd.com/)
- [twitter](https://twitter.com/_kiyotd)
- [github](https://github.com/kiyotd)
