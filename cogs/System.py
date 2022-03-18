import discord
from discord.ext import commands
import os


class System(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command(aliases=["ping", "systeminfo"])
    async def status(self, ctx):
        exts = [
            f"{filename[:-3]}" for filename in os.listdir("./cogs/") if filename.endswith(".py")
        ]
        extsf = "\n".join(exts)

        embed = discord.Embed(
            title="Twilight Dawn | Bot Status",
            description=f"Bot Ping: {round(self.bot.latency * 200)}ms\n"
                        f"\n"
                        f"__Loaded Extensions:__\n"
                        f"{extsf}"
        )
        await ctx.reply(embed=embed)

    @commands.command()
    async def reload(self, ctx, extension):
        try:
            self.bot.reload_extension(f"cogs.{extension}")

            embed = discord.Embed(title='Reload', description=f'{extension} successfully reloaded.',
                                  color=discord.Color.green())
            await ctx.send(embed=embed)
        except discord.ExtensionError:
            embed = discord.Embed(title='Reload',
                                  description=f'{extension} not found.',
                                  color=discord.Color.red())
            await ctx.reply(embed=embed)


    @commands.command(aliases=["hilfe", "bittehelfensiemir"])
    async def help(self, ctx, category: str = None):
        if category is None:
            exts = [
                f"{filename[:-3]}" for filename in os.listdir("./cogs/") if filename.endswith(".py")
            ]
            extsf = "\n".join(exts)
            embed = discord.Embed(
                title="🛠️ | Help Menü",
                description="__Verfügbare  Kategorien:__\n"
                            f"{extsf}\n"
                            f"\n"
                            f"__Permission Level:__\n"
                            f"<:Perm1:954459834902794280> Permission Stufe 1 (User)\n"
                            f"<:Perm2:954459836366618654> Permission Stufe 2 (Sup)\n"
                            f"<:Perm3:954459834835669053> Permission Stufe 3 (Mod)\n"
                            f"<:Perm4:954459834735009933> Permission Stufe 4 (Admin)\n"
                            f"\n"
                            f"__Command Usage Platzhalter:__\n"
                            f"<> - Muss angegeben werden\n"
                            f"[] - Kann angegeben werden\n"
                            f"\n"
                            f"`!help <Kategorie>`"
            )
            await ctx.reply(embed=embed)
            return True
        else:
            if category.upper() == "MODERATION":
                embed = discord.Embed(
                    title="🛠️ | Help Menü",
                    description=f"**!warn**\n"
                                f"`!warn <user> [grund]`\n"
                                f"*Verwarne einen User.*\n"
                                f"\n"
                                f"**!kick**\n"
                                f"`!kick <user> [grund]`\n"
                                f"*Kicke einen User.*\n"
                                f"\n"
                                f"**!softban**\n"
                                f"`!softban <user> [grund]`\n"
                                f"*Banne einen Nutzer mit Chance auf Entbannung.*\n"
                                f"\n"
                                f"**!ban**\n"
                                f"`!ban <user> [grund]`\n"
                                f"*Banne einen User ohne Chance auf Entbannung*\n"
                                f"\n"
                                f""
                )
                await ctx.reply(embed=embed)



def setup(bot):
    bot.add_cog(System(bot))