import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
import os


load_dotenv()


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command()
    async def warn(self, ctx):
        pass

    @commands.command()
    async def kick(self, ctx, user = None, reason: str = None):
        modrole = get(ctx.guild.roles, id=int(os.getenv("MODID")))

        if modrole in ctx.author.roles:
            if user is not None:
                try:
                    if ctx.message.mentions[0] is not None:
                        user = ctx.message.mentions[0]
                except Exception as e:
                    try:
                        if self.bot.get_user(int(user)) is not None:
                            user = self.bot.get_user(int(user))
                        else:
                            await ctx.reply(embed=discord.Embed(title="Twilight Dawn Moderation",
                                                                description="User nicht gefunden."))
                            return True
                    except Exception as e2:
                        await ctx.reply(embed=discord.Embed(title="Twilight Dawn Moderation",
                                                            description="User nicht gefunden."))
                        return True


                if reason is not None:
                    await user.kick(reason=reason)
                else:
                    await ctx.guild.get_member(user.id).kick()
                    await ctx.reply(embed=discord.Embed(
                        title="Twilight Dawn Moderation",
                        description=f"{user.mention} wurde vom Server gekickt."
                    ))
            else:
                await ctx.reply(embed=discord.Embed(title="Twilight Dawn Moderation", description="Bitte gib einen User an."))

        else:
            await ctx.reply(embed=discord.Embed(title="Twilight Dawn Moderation", description="Dazu hast du keine Rechte."))


    @commands.command()
    async def softban(self, ctx):
        pass

    @commands.command()
    async def ban(self, ctx):
        pass


def setup(bot):
    bot.add_cog(Moderation(bot))
