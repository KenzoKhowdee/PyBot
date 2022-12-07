import discord
import random
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("TOKEN")
def main():
  intents = discord.Intents.default()
  intents.message_content = True
  bot = commands.Bot(command_prefix = ">", self_bot =True,intents=intents)
  client = discord.Client(intents=intents)
  @bot.event
  async def on_ready():
    print(f'{bot.user.name} is now running!')
  @bot.command()
  async def guess_game(ctx, num: int):
    ''' A guessing game with the parameters between 1 to 10.'''
    correct = random.randint(1,10)
    if num == correct:
      await ctx.send("{} was the correct guess!".format(num))
    elif num > 10 and num < 1:
      await ctx.send("You need a number between 1 and 10.")
    else:
      await ctx.send("Incorrect, {} was the answer. Please try again!".format(correct))
  @bot.command()
  async def who(ctx):
    await ctx.send("asked???? :)")
  @bot.command()
  async def what(ctx):
    await ctx.send("made you think I asked????? :D")
  @bot.command()
  async def flipcoin(ctx):
    '''This returns heads or tails once the coin is flipped.'''
    correct = random.randint(1,2)
    if correct == 1:
      await ctx.send("heads")
    if correct == 2:
      await ctx.send("tails")
  @bot.command()    
  async def roll(ctx):
    '''This returns a dice roll from 1 to 6'''
    dice = random.randint(1,6)
    await ctx.send("you rolled {}".format(dice))
  @bot.command()
  async def joined(ctx, who: discord.Member):
    await ctx.send(who.joined_at)
  bot.run(token)
if __name__ == "__main__":
  main()
