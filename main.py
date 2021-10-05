import discord
import os
import time
import random

from discord.ext import commands
from discord.ext.commands import *
from upkeep import upkeep
from asyncio import sleep



prefix = '!'


bot = commands.Bot(
  command_prefix=prefix
)



login = os.environ['TOKEN']

# When logged in announce to console.
@bot.event
async def on_ready():
  print(f'Ready! Logged in as {bot.user.name}')

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, CommandNotFound):
    await ctx.reply(":x: Oops, That command doesn't exist!", delete_after=1.5)
  elif isinstance(error, MissingPermissions):
    await ctx.reply(":x: Oops, You don't have permission run this command!", delete_after=1.5)
    
#https://www.youtube.com/watch?v=9ZZWrw-oEVs

@bot.command()
@has_permissions(manage_messages=True)
async def purge(ctx, number: int=None):
  if number is None:
    await ctx.reply(":x: Oopsie, you didn't specify a number silly!", delete_after=1.5)
  elif number >= 101:
    await ctx.reply(":x: Oopsie, i can't remove that many messages!", delete_after=1.5)
  elif number <= 0:
    await ctx.reply(":x: Oopsie, i can't remove that little messages!", delete_after=1.5)
  else:
    deleted = await ctx.channel.purge(limit=number + 1)
    await ctx.channel.send(f'Deleted [{len(deleted) - 1}] message(s)! ({ctx.author.mention})', delete_after=1.5)

@bot.command()
@has_permissions(ban_members = True)
async def kill(ctx, member :  discord.Member, *,reason=None):
    if member == None or member == ctx.message.author:
      if str(ctx.message.author) == 'PeeblYweeb#4200':
        await ctx.reply("You can't kill yourself.. are you suicidal or something?\n...oh wait you're peebly you are.")
        return
      await ctx.reply("You can't kill yourself.. are you suicidal or something? ")
      return
    if reason == None:
        reason = "...wait no reason was provided.. you we're just killed"
    message = f"{member} fell out of the world.\n jk.. but you did get killed for {reason}"
    await member.send(message)
    if str(member) == 'PeeblYweeb#4200':
      await member.send("i bet you liked that didn't you...")
    await member.ban(reason=reason)
    await ctx.send(f"{member} fell out of the world.. ({reason})")

@bot.command()
@has_permissions(kick_members=True)
async def knockout(ctx, member: discord.Member, *, reason=None):
    if member == None or member == ctx.message.author:
      if str(ctx.message.author) == 'PeeblYweeb#4200':
        await ctx.reply("Listen, i know it's a good escape to life but.. Really?\n How do you even expect to do that?")
        return
      await ctx.reply("How do you expect to knock yourself out?")
      return
    await member.send("You we're knocked out! You can still come back!")
    if str(member) == 'PeeblYweeb#4200':
      await member.send("You hoped you died didn't you?")
    await client.kick(member)
    await ctx.send(f'{member} was knocked out.'

@bot.command()
async def ultradrip(ctx):
  await ctx.reply('ooh, this is a fun one! https://www.youtube.com/watch?v=e8gPObK4sQs')

@bot.command()
async def insult(ctx):
  insults = ["Your personality is worse than the roblox management team", "How unmotivated do you have to be to ask a bot to insult you?", "I bet your browser history is dirtier than my feet.", "I'm a Mother fucker, but you are a motherfucker", "I fucked your mom", "Hey Hey! Fun Fact! NOBODY FUCKING CARES, GO SHUT YOUR BITCH ASS UP AND STOP ASKING ME TO INSULT YOU YOU MELTY CREAM LOOKIN ASS", "PeeblyWeeb is cooler than you.", "No, i don't think i will.", "You're that type of person that even when you leave the vc people still are traumitized on how stupid you are.", "bad"]
  if str(ctx.message.author) == 'PeeblYweeb#4200':
    await ctx.send(ctx.author.mention + ' kys')
    return
  await ctx.send(ctx.author.mention + ' ' + random.choice(insults))

# Log into the bot and keep bot online
upkeep()
bot.run(login)
