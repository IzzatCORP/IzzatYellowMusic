import nextcord
from nextcord.ext import commands

from music_cog import music_cog
from main_cog import main_cog

bot = commands.Bot(command_prefix='izz+')

bot.remove_command('help')

bot.add_cog(music_cog(bot))
bot.add_cog(main_cog(bot))

bot.run('your token')