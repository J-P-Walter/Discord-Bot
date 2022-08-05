from .model import GuessAWord
import random

games = {}

class GuessAWordGame:

    current_game = None

    def fetch_game(self):
        return self.current_game

    def create_game_instance(self, channel_id, channel_name):
        random_instance = self.get_random_word()
        new_game = GuessAWord(random_instance['word'], random_instance['category'])
        new_game.channel_id = channel_id
        new_game.channel_name = channel_name
        return new_game

    async def start_game(self, guild, author, players):
        channel_name = "gaw-game-%s" %author.name
        if self.get_channel_by_name(guild, channel_name) is None:
            channel = await self.create_channel(guild, channel_name)
            await self.set_permissions(guild, channel, players)

            new_game = self.create_game_instance(channel.id, channel.name)

            self.save(new_game)
            self.get_game(channel.id)

            return channel
        return None

    def new_round(self, channel):
        self.current_game = None
        new_game = self.create_game_instance(channel.id, channel.name)
        self.save(new_game)
        self.get_game(channel.id)
        return new_game

    def guess(self, channel_id, guess):
        self.get_game(channel_id)
        if self.current_game is None:
            return None
        return self.current_game.guess(guess)

    def get_game(self, channel_id):
        self.current_game = None
        for g in games.keys():
            if g == channel_id:
                self.current_game = games[g]
                break

    def save(self, game):
        games[game.channel_id] = game

    async def destroy(self, channel_id, guild):
        games.pop(channel_id)
        await self.delete_channel(channel_id, guild)

    async def delete_channel(self, channel_id, guild):

        channel = guild.get_channel(channel_id)
        await channel.delete()

    async def set_permissions(self, guild, channel, players):
        await channel.set_permissions(guild.default_role, view_channel=False, send_messages=False)
        for p in players:
            await channel.set_permissions(p, view_channel=True, send_messages=True)

    async def create_channel(self, guild, channel_name):
        category = self.get_category_by_name(guild, "Games")
        await guild.create_text_channel(channel_name, category=category)
        channel = self.get_channel_by_name(guild, channel_name)
        return channel

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
        return random.choice([
            {
                'word': 'python',
                'category': "development"
            },
            {
                'word': 'tree',
                'category': "nature"
            },
            {
                'word': 'league',
                'category': "legends"
            }
        ])