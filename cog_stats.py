from discord.ext import commands
import api_handler

class CodStats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='rankedstats')
    async def fetch_ranked_stats(self, ctx, player: str):
        stats = api_handler.get_ranked_stats(player)
        await ctx.send(f"Ranked Stats for {player}: {stats}")

def setup(bot):
    bot.add_cog(CodStats(bot))
