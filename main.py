import config
import logging
import duties.splatoon2
import duties.servernamechange
import discord
from discord.ext import commands


logging.basicConfig(level=logging.INFO)
bot = commands.Bot(command_prefix='?', description='hoge')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


bot.add_cog(duties.splatoon2.Splatoon2(bot=bot))
bot.add_cog(duties.servernamechange.ServerNameChange(bot=bot))
bot.run(config.SHIRO_BOT_DISCORD_TOKEN)
