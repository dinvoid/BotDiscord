import discord
from discord.ext import commands

# Set up bot intents
intents = discord.Intents.default()
intents.members = True  # Enable member updates
intents.message_content = True  # Enable message content

# Create bot instance with intents
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    # Send welcome message
    welcome_channel = discord.utils.get(member.guild.text_channels, name="general")
    if welcome_channel:
        await welcome_channel.send(f'Hi {member.mention}, maayo kay mi join ka! 🎉')

    # Add member to "play" channel
    play_channel = discord.utils.get(member.guild.text_channels, name="play-chess")
    if play_channel:
        await play_channel.set_permissions(member, read_messages=True, send_messages=True)


bot.run('your_token')
