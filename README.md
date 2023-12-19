
# TwitchTranslateBot

Welcome to the `Twitch Translate Bot` repository! This bot is designed to enhance the interactivity and accessibility of Twitch streams by providing real-time translation of chat messages. It's an ideal tool for streamers and viewers looking to bridge language barriers and engage with a global audience.

## Features

- **Real-Time Translation**: Instantly translates messages in Twitch chat to a specified language using Google Translate, making the stream more accessible to a diverse audience.
- **Customizable Language Settings**: Configure the target language for translation and specify languages to ignore in the `config.py` file.
- **Easy to Use**: Simply type `!translate` followed by the message you want to translate in the chat, and the bot will respond with the translated text.

## Configuration

Before using the TwitchTranslateBot, you need to set up your configuration in the `config.py` file. Here are the steps to get started:

1. **Set up Twitch Bot Credentials**:
    - `TOKEN`: Your Twitch OAuth token. Obtain it from [Twitch Chat OAuth Password Generator](https://twitchapps.com/tmi/).
    - `BOT_NAME`: The username of your Twitch bot.
    - `CHANNEL`: The Twitch channel where the bot will operate.

2. **Set up Translation Settings**:
    - `DEST_LANGUAGE`: The target language for translations (e.g., 'es' for Spanish).
    - `IGNORE_LANGUAGES`: List of language codes that the bot should not translate.

## Installation

To install TwitchTranslateBot, clone this repository and install the required Python packages:

```bash
git clone https://github.com/jesus0m/twitch-translate-bot.git
cd twitch-translate-bot
pip install -r requirements.txt
```

## Running the Bot

To run the bot, execute the main script from the command line:

```bash
python translate-bot.py
```

Replace `bot_script_name.py` with the name of your bot's script file.

## Usage

In your Twitch chat, use the command `!translate` followed by the text you want to translate. For example:

```
!translate Hello, how are you?
```

The bot will respond with the translated text in the chat.

## Contributing

Contributions to Twitch Translate Bot are welcome! Feel free to fork the repository, make changes, and submit pull requests. If you encounter any issues or have suggestions, please open an issue in the repository.

---

Thank you for supporting TwitchTranslateBot!
