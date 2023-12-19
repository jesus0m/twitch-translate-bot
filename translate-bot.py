# Imports
from googletrans import Translator
from twitchio.ext import commands

import config


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=config.TOKEN, prefix='!', initial_channels=[config.CHANNEL], nick=config.BOT_NAME)

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

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
            translation = translator.translate(text_to_translate, dest=config.DEST_LANGUAGE)
            if translation.src in config.IGNORE_LANGUAGES:
                return  # Ignore the translation if the source language is in the ignore list

            translated_text = translation.text
            src_language_code = translation.src  # Using the language code
            dest_language_code = config.DEST_LANGUAGE  # Using the target language code

            await ctx.send(f"{translated_text} [by {ctx.author.name}] ({src_language_code} > {dest_language_code})")
        except Exception as e:
            await ctx.send("Translation error.")
            print(f"Error: {e}")

if __name__ == "__main__":
    bot = Bot()
    bot.run()
