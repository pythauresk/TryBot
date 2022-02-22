import os

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv(dotenv_path="config")


class TryBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/")

    async def on_ready(self):  # pas besoin de décorateurs
        print(f"{self.user.display_name} est connecté")


bot = TryBot()


@bot.command(name='del')
# extrait de https://www.youtube.com/watch?v=SLd4d5EqbiM
async def delete(ctx, number_of_messages: int):  # ctx le contexte d'appel de la commande
    messages = await ctx.channel.history(limit=number_of_messages+1).flatten()
    for msg in messages:
        await msg.delete()  # suppression

# TODO creer une collection de commandes cog et inserer une ligne
# bot.add_cog(set)  un setup des commandes dans la classe Trybot

# voir ça https://github.com/AlexFlipnote/discord_bot.py/blob/master/cogs/fun.py
# et la doc de discordpy https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#cog

bot.run(os.getenv("TOKEN"))

