# Imports
from googletrans import Translator
from twitchio.ext import commands
import os
import sys


def load_config():
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.dirname(__file__)

    config_path = os.path.join(application_path, 'config.py')

    config = {}
    if os.path.isfile(config_path):
        with open(config_path) as f:
            exec(f.read(), config)
    else:
        print("Config file not found.")
        sys.exit(1)
    return config


class Bot(commands.Bot):

    def __init__(self, config):
        super().__init__(token=config['TOKEN'], prefix='!', initial_channels=[config['CHANNEL']],
                         nick=config['BOT_NAME'])
        self.config = config
        self.my_initial_channels = [config['CHANNEL']]  # Almacenar los canales iniciales en una propiedad personalizada

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        welcome_message = self.config['WELCOME_MESSAGE']

        for channel_name in self.my_initial_channels:
            channel = self.get_channel(channel_name)
            if channel:
                await channel.send(welcome_message)

    async def event_message(self, message):
        if message.echo:
            return

        await self.handle_commands(message)

    @commands.command(name='translate')
    async def translate(self, ctx):
        translator = Translator()
        text_to_translate = ctx.message.content[len('!translate '):].strip()
        if not text_to_translate:
            return await ctx.send("Please provide a message to translate.")

        # Translate the message
        try:
            translation = translator.translate(text_to_translate, dest=self.config['DEST_LANGUAGE'])
            if translation.src in self.config['IGNORE_LANGUAGES']:
                return  # Ignore the translation if the source language is in the ignore list

            translated_text = translation.text
            src_language_code = translation.src
            dest_language_code = self.config['DEST_LANGUAGE']

            await ctx.send(f"{translated_text} [by {ctx.author.name}] ({src_language_code} > {dest_language_code})")
        except Exception as e:
            await ctx.send("Translation error.")
            print(f"Error: {e}")


if __name__ == "__main__":
    config = load_config()
    bot = Bot(config)
    bot.run()
