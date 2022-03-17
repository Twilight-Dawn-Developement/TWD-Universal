import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
import os


load_dotenv()


class Moderation(commands.Cog):
    def __init__(self, bot):
        bot: commands.Bot = bot

    @commands.command()
    async def warn(self, ctx):
        await ctx.reply("works")

    @commands.command()
    async def kick(self, ctx, user = None, reason: str = None):
        modrole = get(ctx.guild.roles, id=int(os.getenv("MODID")))

        if ctx.author.has_role(modrole):
            if user is not None:
                if reason is not None:
                    await user.kick(reason=reason)
                else:
                    await user.kick()
            else:
                ctx.reply(embed=discord.Embed(title="Twilight Dawn Moderation", description="Bitte gib einen User an."))


    @commands.command()
    async def softban(self, ctx):
        await ctx.reply("works")

    @commands.command()
    async def ban(self, ctx):
        await ctx.reply("works")


def setup(bot):
    bot.add_cog(Moderation(bot))