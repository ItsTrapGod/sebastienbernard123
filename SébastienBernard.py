import discord
import youtube_dl
from discord.ext import commands



TOKEN = 'NDk3OTMxODQzODg3MzAwNjI4.DpmW4w.Z4F_W8PjJGBDhat6PUwJUeE4B10'

client = commands.Bot(command_prefix = "!")
client.remove_command('help')



players = {}
queues = {}
extensions = ['fun']





def check_queue(id):
    if queues[id] != []:
        player = queues[id].pop(0)
        players[id] = player
        player.start()




@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="!help for commands", url="https://www.twitch.tv/itstrapgod", type=1))
    print("I am alive!")




# Load & Unload Command

@client.command()
async def load(extension):
    try:
        client.load_extension(extension)
        print('Loaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be loaded. [{}]'.format(extension, error))


@client.command()
async def unload(extension):
    try:
        client.unload_extension(extension)
        print('Unloaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be unloaded. [{}]'.format(extension, error))



if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))



# Info Command

@client.command()
async def info():
    embed = discord.Embed(
        title = 'Creator: Paul#6060',
        description = 'Created Using Python Version 3.6.5',
        colour = discord.Colour.blue()
        )


    embed.set_footer(text='Made With Love :)')
    embed.set_image(url='https://bit.ly/2KaEkhk')
    embed.set_author(name='Sébastien Bernard',
    icon_url='https://media.discordapp.net/attachments/512768412003467276/545284254482038807/Astolfo_Profile_Picture.png')
    embed.add_field(name='Bot Version', value = '1.0.4', inline=False)
    embed.add_field(name='Last Updated', value = 'February 13th 2019', inline=False)
    embed.add_field(name="What's New?", value = 'Added The Mig Custom Command', inline=False)

    await client.say(embed=embed)


# Help Command

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
        )

    embed.set_author(name='Help')
    embed.add_field(name='!info', value='Gives Embeded Information About The Bot', inline=False)
    embed.add_field(name='!play [URL]', value='Plays Audio From a YouTube Video', inline=False)
    embed.add_field(name='!join', value='Makes the Bot Join a Voice Channel [You Must be in the Same Voice Channel for it to Join]', inline=False)
    embed.add_field(name='!leave', value='Makes the Bot Leave a Voice Channel [You Must be in the Same Voice Channel for it to Leave]', inline=False)
    embed.add_field(name='!pause', value='Pauses Currently Playing Song', inline=False)
    embed.add_field(name='!resume', value='Resumes The Paused Song', inline=False)
    embed.add_field(name='!skip', value='Skips To The Next Song In The Queue. Stops Playing Songs If No Songs Are In Queue', inline=False)
    embed.add_field(name='!next [URL]', value='Adds The Song To The Queue', inline=False)
    embed.add_field(name='!fotd', value='Displays The Fact of The Day', inline=False)
    embed.add_field(name='!skrr', value='Secret Command #1', inline=False)
    embed.add_field(name='!dragon', value='Secret Command #2', inline=False)
    embed.add_field(name='!niggers', value='Secret Command #3', inline=False)
    embed.add_field(name='!amine', value='Secret Command #4', inline=False)
    embed.add_field(name='!milly', value='Secret Command #5', inline=False)
    embed.add_field(name='!mig', value='Secret Command #6', inline=False)


    await client.send_message(author, embed=embed)



# Joining & Leaving Voice Chat

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    embed = discord.Embed(
    title = 'I have joined the voice channel',
    colour = discord.Colour.green()
    )

    await client.say(embed=embed)



@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()
    embed = discord.Embed(
    title = 'I have left the voice channel',
    colour = discord.Colour.red()
    )

    await client.say(embed=embed)




# Play Command

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
    players[server.id] = player
    player.start()



# Pause, Stop & Resume Commands

@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()
    embed = discord.Embed(
    title = 'Song has been paused',
    colour = discord.Colour.gold()
    )

    await client.say(embed=embed)


@client.command(pass_context=True)
async def skip(ctx):
    id = ctx.message.server.id
    players[id].stop()
    embed = discord.Embed(
    title = 'Song has been skipped',
    colour = discord.Colour.light_grey()
    )

    await client.say(embed=embed)


@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()
    embed = discord.Embed(
    title = 'Song has been resumed',
    colour = discord.Colour.dark_green()
    )

    await client.say(embed=embed)



# Queue

@client.command(pass_context=True)
async def next(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))


    if server.id in queues:
        queues[server.id].append(player)
    else:
        queues[server.id] = [player]
        embed = discord.Embed(
        title = 'Song has been added to the queue',
        colour = discord.Colour.dark_green()
        )

        await client.say(embed=embed)





client.run(TOKEN)
