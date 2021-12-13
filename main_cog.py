import nextcord
from nextcord.ext import commands

class main_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
My prefix is `izz+`

Play = play <title or url youtube> - playing some music added

Queue = queue - show queue music

Skip = skip - skip playing

Disconnect = disconnect - disconnect in voice channel

Created by IzzatCORP
"""
        self.text_channel_list = []

    #some debug info so that we know the bot has started    
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)

    @commands.command()
    async def help(self, ctx):
        await ctx.send(self.help_message)