import datetime
import random
import logging
import discord
from discord.ext import tasks, commands


class ServerNameChange(commands.Cog):
    kanji_table = {'0': '〇', '1': '一', '2': '二', '3': '三', '4': '四', '5': '五', '6': '六', '7': '七', '8': '八', '9': '九'}
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='サーバ名自動変更')
    async def name_change(self, ctx):
        num = random.randint(1, 100)
        
        kanji = ''.join([self.kanji_table[s] for s in str(num)]) + '（仮）'
        logging.info(f'Server name changed to {kanji} by command.')
        await ctx.guild.edit(name=kanji)
