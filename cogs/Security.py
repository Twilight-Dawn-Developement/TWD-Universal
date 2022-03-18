import os
from datetime import datetime

from discord.ext import commands
import discord


class Security(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.Cog.listener("on_member_join")
    async def on_member_join(self, member):  # Überprüft neue Member
        points = 0
        member_days = (datetime.utcnow() - member.created_at).days
        if member_days <= 10:  # Falls der Account jünger als 4 Tage ist ban Rolle
            points += 25
            print(f'{member} ({member.id}) user <= 10 days old ({member_days}) | +25 points')
        elif member_days <= 15:  # jünger als 15
            points += 15
            print(f'{member} ({member.id}) user <= 15 days old ({member_days}) | +15 points')
        elif member_days <= 30:
            points += 10
            print(f'{member} ({member.id}) user <= 30 days old ({member_days}) | +10 points')
        elif member_days <= 80:
            points += 5
            print(f'{member} ({member.id}) user <= 80 days old ({member_days}) | +5 points')
        url = member.avatar_url
        if "/embed/" in str(url).lower():  # Falls Standart Avatar
            points += 15
            print(f'{member} ({member.id}) no avatar | +15 points')
        if "gg/" in member.name or ".io" in member.name or "fuck" in member.name or "wiz" in member.name or "nuke" in member.name or "sellix" in member.name or "Sellix" in member.name or "Nuke" in member.name or "Wiz" in member.name:  # Viele Bots haben den Invite Link zum Server wo die Tokens verkauft wurden im Namen -> hier die kontrolle
            points += 25
            print(f'{member} ({member.id}) blacklisted word in username | +25 points')
        if points >= 25:  # Festlegen von Punktzahl wo der Bot handelt (hier ändern falls nötig)
            ban = discord.utils.get(member.guild.roles, id=int(os.getenv("UnverifiedID")))
            await member.add_roles(ban, reason='Possible Alt')
            embed = discord.Embed(title="Twilight Dawn Security System",
                                  description=f'Dir wurde aus Sicherheitsgründen die unverified Rolle gegeben. Falls du '
                                              f'trotzdem den Server weiter nutzen willst gehe in '
                                              f'<#{int(os.getenv("VerifyTicketID"))}>!',
                                  # Hier Invite ändern
                                  color=discord.Color.red())
            try:
                await member.send(embed=embed)
            except Exception:
                pass

            embedteam = discord.Embed(title="Twilight Dawn Security System",
                                      description=f"{member} <@{member.id}> ({member.id}) wurde wegen Possible Alt die "
                                                  f"unverified Rolle gegeben. Account erstellt: {member.created_at}",
                                      color=discord.Color.red())
            channel = self.bot.get_channel(int(os.getenv("AntiAltLogs")))
            await channel.send(embed=embedteam)
            print(f'Banned {member} | points: {points}')


def setup(bot: commands.Bot):
    bot.add_cog(Security(bot))
