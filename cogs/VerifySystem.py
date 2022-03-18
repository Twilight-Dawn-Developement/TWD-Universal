import asyncio

import discord
from discord.ext import commands


class VerifySystem(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command(aliases=["v"])
    @commands.has_role("verify-sup")
    async def verify(self, ctx,
                     member: discord.Member = None):  # Zum Hinzufügen von Admins zum kontrollieren des Bots auf beiden guilds
        if member is None:
            respone = await ctx.send('gib einen ID an / tag jemanden')
            await asyncio.sleep(3)
            await ctx.message.delete()
            await respone.delete()
        else:
            role = discord.utils.get(member.guild.roles, id=920792838587953223)
            await member.remove_roles(role, reason='Verify')
            respone = await ctx.send(f'Verified {member}')
            await asyncio.sleep(1)
            await ctx.message.delete()
            embedteam = discord.Embed(title="Twilight Dawn Verify System",
                                      description=f"{member} ({member.id}) wurde von {ctx.message.author.name} ({ctx.message.author.id}) verifiziert.",
                                      color=discord.Color.red())
            channel = self.bot.get_channel(933103397794611280)
            await channel.send(embed=embedteam)

    @commands.command(aliases=["h", "h+"])
    @commands.has_role("verify-sup")
    async def handyuser(self, ctx,
                        member: discord.Member = None):  # Zum Hinzufügen von Admins zum kontrollieren des Bots auf beiden guilds
        if member is None:
            respone = await ctx.send('gib einen ID an / tag jemanden')
            await asyncio.sleep(3)
            await ctx.message.delete()
            await respone.delete()
        else:
            role = discord.utils.get(member.guild.roles, name="verifying")
            await member.add_roles(role, reason='verifing role')
            respone = await ctx.send(f'Gave {member} verifing role')
            await asyncio.sleep(1)
            await ctx.message.delete()
            embedteam = discord.Embed(title="Twilight Dawn Verify System",
                                      description=f"{member} ({member.id}) wurde von {ctx.message.author.name} ({ctx.message.author.id}) die verifing Rolle gegeben.",
                                      color=discord.Color.red())
            channel = self.bot.get_channel(933103397794611280)
            await channel.send(embed=embedteam)

    @commands.command(aliases=["h-", "n"])
    @commands.has_role("verify-sup")
    async def noverifying(self, ctx,
                          member: discord.Member = None):  # Zum Hinzufügen von Admins zum kontrollieren des Bots auf beiden guilds
        if member is None:
            respone = await ctx.send('gib einen ID an / tag jemanden')
            await asyncio.sleep(3)
            await ctx.message.delete()
            await respone.delete()
        else:
            role = discord.utils.get(member.guild.roles, name="verifying")
            await member.remove_roles(role, reason='verifing role')
            respone = await ctx.send(f'Removed verifing role for {member}')
            await asyncio.sleep(1)
            await ctx.message.delete()
            embedteam = discord.Embed(title="Twilight Dawn Verify System",
                                      description=f"{member} ({member.id}) wurde von {ctx.message.author.name} ({ctx.message.author.id}) die verifing Rolle entzogen.",
                                      color=discord.Color.red())
            channel = self.bot.get_channel(933103397794611280)
            await channel.send(embed=embedteam)

    @commands.command(aliases=["b"])
    @commands.has_role("verify-sup")
    async def verifyban(self, ctx,
                  member: discord.Member = None):  # Zum Hinzufügen von Admins zum kontrollieren des Bots auf beiden guilds
        role = discord.utils.get(member.guild.roles, id=920792838587953223)
        if member is None or member == ctx.message.author or role not in member.roles:
            respone = await ctx.send('gib einen gültigen User / gib eine gültige ID an / tag jemanden')
            await asyncio.sleep(3)
            await ctx.message.delete()
            await respone.delete()
        else:
            reason = f'Banned by {ctx.message.author.name} ({ctx.message.author.id})'
            await ctx.guild.ban(member, reason=reason)
            respone = await ctx.send(f'Banned {member} by {ctx.message.author.name} ({ctx.message.author.id})')
            await asyncio.sleep(1)
            await ctx.message.delete()
            embedteam = discord.Embed(title="Twilight Dawn Verify System",
                                      description=f"{member} ({member.id}) wurde von {ctx.message.author.name} ({ctx.message.author.id}) gebannt.",
                                      color=discord.Color.red())
            channel = self.bot.get_channel(933103397794611280)
            await channel.send(embed=embedteam)

    @commands.command(aliases=["m"])
    @commands.has_role("verify-sup")
    async def move(self, ctx,
                   member: discord.Member = None):  # Zum Hinzufügen von Admins zum kontrollieren des Bots auf beiden guilds
        channel = member.voice.channel
        if member is None:
            respone = await ctx.send('gib eine gültige ID an / tag jemanden')
            await asyncio.sleep(3)
            await ctx.message.delete()
            await respone.delete()
        elif channel.id == 920798809074855936:
            channel = self.bot.get_channel(933099449188765748)
            await member.move_to(channel)
            respone = await ctx.send(
                f'Moved {member} by {ctx.message.author.name} ({ctx.message.author.id}) to {channel.name}')
            await asyncio.sleep(1)
            await ctx.message.delete()

    @commands.command(aliases=["d"])
    @commands.has_role("verify-sup")
    async def disconnect(self, ctx,
                         member: discord.Member = None):  # Zum Hinzufügen von Admins zum kontrollieren des Bots auf beiden guilds
        if member is None:
            respone = await ctx.send('gib eine gültige ID an / tag jemanden')
            await asyncio.sleep(3)
            await ctx.message.delete()
            await respone.delete()
        else:
            channel = member.voice.channel
            if channel.id == 933099449188765748:
                await member.move_to(None)
                respone = await ctx.send(
                    f'Disconnected {member} by {ctx.message.author.name} ({ctx.message.author.id}) from {channel.name}')
                await asyncio.sleep(1)
                await ctx.message.delete()
            else:
                respone = await ctx.send('nicht zu Verify SUpport verbunden')
                await asyncio.sleep(3)
                await ctx.message.delete()
                await respone.delete()


def setup(bot: commands.Bot):
    bot.add_cog(VerifySystem(bot))