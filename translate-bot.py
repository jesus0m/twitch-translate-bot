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
        # Divide el mensaje en palabras y elimina el comando '!translate'
        parts = ctx.message.content.split(' ')[1:]
        
        # Asume que el idioma de destino es el idioma de destino predeterminado
        dest_language = self.config['DEST_LANGUAGE']
        text_to_translate = ' '.join(parts)
        
        # Si el primer argumento es un código de idioma válido de dos letras, úsalo como idioma de destino
        if parts and len(parts[0]) == 2 and parts[0].isalpha():
            dest_language = parts[0].lower()
            text_to_translate = ' '.join(parts[1:])
        
        if not text_to_translate:
            return await ctx.send("Please provide a message to translate.")

        # Realiza la traducción con el idioma de destino proporcionado o el predeterminado
        try:
            translation = translator.translate(text_to_translate, dest=dest_language)
            if translation.src in self.config['IGNORE_LANGUAGES']:
                return  # Ignora la traducción si el idioma de origen está en la lista de ignorados

            translated_text = translation.text
            src_language_code = translation.src
            dest_language_code = translation.dest

            await ctx.send(f"{translated_text} [translated by {ctx.author.name}] ({src_language_code} > {dest_language_code})")
        except Exception as e:
            await ctx.send("Translation error.")
            print(f"Error: {e}")


if __name__ == "__main__":
    config = load_config()
    bot = Bot(config)
    bot.run()
