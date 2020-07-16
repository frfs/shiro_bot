import datetime
import json
import discord
from discord.ext import commands
import requests


'''
スプラトゥーン2絡みのコマンド
'''
class Splatoon2(commands.Cog, name="スプラトゥーン2"):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="SalmonSchedule")
    async def say_salmon_schedule(self, ctx):
        '''サーモンランのスケジュールを出す'''
        url = 'https://spla2.yuu26.com/coop/schedule'
        ua = 'ShiroBot/1.0 (@frfr@mstdn.f72u.net)'
        headers = {'User-Agent': ua}

        template = '''
直近:
・ステージ: {0}
・時間: {1}～{2}
・ブキ: {3}

次:
・ステージ: {4}
・時間: {5}～{6}
・ブキ: {7}
        '''

        ret = requests.get(url, headers=headers)
        if (ret.status_code == 200):
            # OK
            data = ret.json()['result']
            await ctx.send(template.format(
                data[0]['stage']['name'],
                data[0]['start'],
                data[0]['end'],
                ','.join([data[0]['weapons'][0]['name'], data[0]['weapons'][1]['name'], data[0]['weapons'][2]['name'], data[0]['weapons'][3]['name']]),
                data[1]['stage']['name'],
                data[1]['start'],
                data[1]['end'],
                ','.join([data[1]['weapons'][0]['name'], data[1]['weapons'][1]['name'], data[1]['weapons'][2]['name'], data[1]['weapons'][3]['name']])
            ))
        else:
            # NG
            await ctx.send('バイトデータの取得に失敗しました')
