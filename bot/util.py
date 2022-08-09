from discord.ext import commands
from settings._global import MOD_ROLE_NAME

def mods_or_owner():
    def predicate(ctx):
        return commands.check_any(commands.is_owner(), commands.has_role(MOD_ROLE_NAME))
    return commands.check(predicate)

async def notify_user(member, message):
    if member is not None:
        channel = member.dm_channel
        if channel is None:
            channel = await member.create_dm()
        await channel.send(message)
