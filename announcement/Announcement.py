import discord
from discord.ext import commands

class AnnouncementPlugin:
    def __init__ (self, Client):
        self.Client = Client

    @commands.command (pass_context = True)
    async def announce (self, ctx, _Title : str, _Message : str, _Channel : discord.Channel):
        Server = ctx.message.server

        Data = await self.Client.LoadConfig (Server.id)

        if 'announce' in Data['Plugins']:
            Embed = discord.Embed (title = _Title, description = _Message, color = Data['EmbedColor'])

            await self.Client.send_message (_Channel, embed = Embed)

def setup (_Client):
    _Client.add_cog (AnnouncementPlugin (_Client))
