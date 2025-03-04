import discord
from discord.ext import commands
import json
import cog_stats

# Load bot settings from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Event triggered when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# Load cog for handling stats
bot.add_cog(cog_stats.CodStats(bot))

# Run the bot
bot.run(config['DISCORD_TOKEN'])
