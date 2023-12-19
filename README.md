
# Twitch Translate Bot

Welcome to the `Twitch Translate Bot` repository! This bot is designed to enhance the interactivity and accessibility of Twitch streams by providing real-time translation of chat messages. It's an ideal tool for streamers and viewers looking to bridge language barriers and engage with a global audience.

## Features

- **Real-Time Translation**: Instantly translates messages in Twitch chat to a specified language using Google Translate, making the stream more accessible to a diverse audience.
- **Customizable Language Settings**: Configure the target language for translation and specify languages to ignore in the `config.py` file.
- **Easy to Use**: Simply type `!translate` followed by the message you want to translate in the chat, and the bot will respond with the translated text.


## Executable Downloads

To facilitate the use of Twitch Translate Bot, executable versions for different operating systems have been provided. Download the executable corresponding to your system, modify the `config.py` file as needed, and run the bot directly.

### macOS

Download for macOS: [translate_bot_v2.0.0_mac_os_x.zip](https://github.com/jesus0m/twitch-translate-bot/releases/download/2.0.0/translate_bot_v2.0.0_mac_os_x.zip)

To run on macOS:
- Unzip the `.zip` file.
- Right-click on `translate-bot.command` and select "Open".
- If this is your first time running a script of this type, you may need to allow it in your Mac's security preferences.

### Windows

Download for Windows: [translate_bot_v2.0.0_windows.zip](https://github.com/jesus0m/twitch-translate-bot/releases/download/2.0.0/translate_bot_v2.0.0_windows.zip)

To run on Windows:
- Extract the `.zip` file.
- Run `translate-bot.exe`.

### Additional Configuration

Before running the bot, be sure to configure the `config.py` file with appropriate details such as your Twitch credentials and language preferences. This file should be located in the same directory as the executable.


## Configuration

Before using the Twitch Translate Bot, you need to set up your configuration in the `config.py` file. Here are the steps to get started:

1. **Set up Twitch Bot Credentials**:
    - `TOKEN`: Your Twitch OAuth token. Obtain it from [Twitch Chat OAuth Password Generator](https://twitchapps.com/tmi/).
    - `BOT_NAME`: The username of your Twitch bot.
    - `CHANNEL`: The Twitch channel where the bot will operate.
    - `WELCOME_MESSAGE`: Customize the bot's startup message which it will send to the chat when it runs for the first time, or otherwise leave it empty if you do not want this message to be displayed.

2. **Set up Translation Settings**:
    - `DEST_LANGUAGE`: The target language for translations (e.g., 'es' for Spanish).
    - `IGNORE_LANGUAGES`: List of language codes that the bot should not translate.

## Installation

To install Twitch Translate Bot, clone this repository and install the required Python packages:

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

Replace `translate-bot.py` with the name of your bot's script file.

## Usage

In your Twitch chat, use the command `!translate` followed by the text you want to translate. For example:

```
!translate Hello, how are you?
```

The bot will respond with the translated text in the chat.

## Contributing

Contributions to Twitch Translate Bot are welcome! Feel free to fork the repository, make changes, and submit pull requests. If you encounter any issues or have suggestions, please open an issue in the repository.

---

Thank you for supporting Twitch Translate Bot!
