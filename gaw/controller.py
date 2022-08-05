from .model import GuessAWord
import random

games = {

}

class GuessAWordGame:

    async def start_game(self, guild, author, players):
        channel_name = "gaw-game-%s" %author.name
        if self.get_channel_by_name(guild, channel_name) is None:
            await self.create_channel(guild, channel_name)
            channel = self.get_channel_by_name(guild, channel_name)
            await self.set_permissions(guild, channel, players)
            return True
        return None

    async def set_permissions(self, guild, channel, players):
        await channel.set_permissions(guild.default_role, view_channel=False, send_messages=False)
        for p in players:
            await channel.set_permissions(p, view_channel=True, send_messages=True)


    async def create_channel(self, guild, channel_name):
        category = self.get_category_by_name(guild, "Games")
        await guild.create_text_channel(channel_name, category=category)

    def get_channel_by_name(self, guild, channel_name):
            channel = None
            for c in guild.channels:
                if c.name == channel_name.lower():
                    channel = c
                    break
            return channel

    def get_category_by_name(self, guild, category_name):
        category = None
        for c in guild.categories:
            if c.name == category_name:
                category = c
                break
        return category
    
    def get_random_word(self):
        return random.choice(('discord', 'bot', 'anime'))