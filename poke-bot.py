import discord
import pypokedex
from discord.ext import commands
import random

# Type matchups 
types = {
    'Fire':'Fire is super effective against Grass/Ice/Bug/Steel, and weak against Water/Rock/Ground',
    'Water':'Water is super effective against Ground/Fire/Rock, and weak against Grass/Electric/',
    'Grass':'Grass is super effective against Water/Ground/Rock, and weak against Bug/Fire/Flying/Ice/Poison',
    'Fighting':'Fighting is super effective against Dark/Ice/Normal/Rock/Steel, and weak against Fairy/Flying/Psychic',
    'Flying':'Flying is super effective against Bug/Fighting/Grass, and weak against Electric/Ice/Rock',
    'Fairy':'Fairy is super effective against Dark/Dragon/Fighting, and weak against Poison/Steel',
    'Ghost':'Ghost is super effective against Ghost/Psycic, and weak against Dark, but immune to normal',
    'Ground':'Ground is super effective against Electric/Fire/Poison/Rock/Steel, and weak against Grass/Ice/Water',
    'Ice':'Ice is super effective against Dragon/Flying/Grass/Ground, and weak against Fighting/Fire/Rock/Steel',
    'Normal':'Normal is super effective against nothing, and weak against fighting, but immune to ghost',
    'Rock':'Rock is super effective against Bug/Fire/Flying/Ice, and weak against Fighting/Grass/Ground/Steel/Water',
    'Steel':'Steel is super effecitve against Fairy/Ice/Rock, and weak against Fighting/Fire/Ground',
    'Dragon':'Dragon is super effective against Dragon, and weak against Fairy/Ice',
    'Dark':'Dark is super effective against Ghost/Psychic, and weak against Bug/Fairy/Fighting',
    'Bug':'Bug is super effective against Grass/Dark/Psychic, and weak against Fire/Flying/Rock',
    'Electric':'Electric is super effective against Flying/Water, and weak against Ground',
    'Psychic':'Psychic is super effective against Fighting/Poison, and weak against Bug/Dark/Ghost',
    'Poison':'Poison is super effective against Fairy/Grass, and weak against Ground Psychic',
}

# Discord bot token
token = ''

# Permissions for bot 
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True 

client = commands.Bot(command_prefix='?',description='fghfgh',intents=intents)

@client.event
async def on_ready():
    print(f'Bot is Ready {client.user}')

# Returns the different commands
@client.command()
async def commands(ntx):
    await ntx.send("Commands: ?mon_type / ?dex / ?goat / ?name")

# Return a type matchup
@client.command()
async def mon_type(ntx : str, type_1: str):
    msg = ''
    if type_1 in types:
        msg = types[type_1]
    else:
        msg = 'That is not a valid Pokemon type try uppercase, the types are case sensitve'
    await ntx.send(msg)

# Return a mon using its dex number
@client.command()
async def dex(num :int,num_1: int):
    dex_num = num_1
    await num.send(pypokedex.get(dex=dex_num).sprites[0]['default'])
    await num.send(pypokedex.get(dex=dex_num).sprites[0]['shiny'])
    await num.send(pypokedex.get(dex=dex_num).name)
    print(pypokedex.get(dex=dex_num).name.upper())

# Return a mon and its ability using its name 
@client.command()
async def name(ntx: str, mon: str):
    await ntx.send(pypokedex.get(name=mon).sprites[0]['default'])
    await ntx.send(pypokedex.get(name=mon).sprites[0]['shiny'])
    await ntx.send('Abilites: '+str(pypokedex.get(name=mon).abilities[0][0])+' | '+str(pypokedex.get(name=mon).abilities[1][0]))
    types = str(pypokedex.get(name=mon).types)
    await ntx.send('Type: '+types)

# Random Pokemon Command
@client.command()
async def goat(ntx: str):
        await ntx.send('SOSA')

# Pokemon stats command
@client.command()
async def stats(ntx: str, stats: str):
    await ntx.send(pypokedex.get(name=stats).base_stats.hp)
    
# Pokemon type chart command 
@client.command()
async def chart(ntx: str):
    img = 'https://cdn.discordapp.com/attachments/756538871126163496/1048133338453528626/460px-Pokemon_Type_Chart.svg.png'
    await ntx.send(img)

# Check if a pokemon can learn a certain move
@client.command()
async def move_check(ntx: str,mon: str,mov: str):
    m = pypokedex.get(name=mon)
    n = [move.name for move in m.moves['sun-moon']]
    msg = ''
    if mov in n:
        msg = 'True'
    else:
        msg = 'False'
    await ntx.send(msg)

client.run(token)
