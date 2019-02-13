import discord
from discord.ext import commands


client = discord.Client()

class Fun:
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def ping(self):
        await self.client.say('Pong!')

    @commands.command()
    async def niggers(self):
        embed = discord.Embed(
            title = 'are NOT people',
            colour = discord.Colour.red()
            )
        await self.client.say(embed=embed)


    @commands.command()
    async def fotd(self):
        await self.client.say('https://www.factslides.com/s-Fact-Of-The-Day')


    @commands.command()
    async def dragon(self):
        await self.client.say('https://bit.ly/2Kgg4ut')


    @commands.command()
    async def skrr(self):
        await self.client.say('GOSH DIDDLE DARN YEEHAW WOT IN TARNATION SLOW DOWN PARTNER https://bit.ly/2DoCLLs')

    @commands.command()
    async def amine(self):
        embed = discord.Embed(
            title = "Grosse marde qui a réussi à s'échapper des égouts dans lequel il est né",
            colour = discord.Colour.red()
            )
        await self.client.say(embed=embed)

    @commands.command()
    async def milly(self):
        embed = discord.Embed(
            title = 'Did I mention that God hates me? Because he does. i am FUCKING homeless AND ITS ALL YOUR FAULT PAUL. ALL.FUCKING.YOURS. YOU MADE ME HOMELESS. I CHEATED ON DOUG BECAUSE OF YOU PAUL. also, I have taken 3 virgini-',
            colour = discord.Colour.red()
            )

    @commands.command()
    async def mig(self):
        embed = discord.Embed(
            title = 'Loves children even though he has an entire inventory of girls to choose from (allegedly). Also is an alcoholic/drug dealing thot hooligan who should be in the hands of the DPJ',
            colour = discord.Colour.red()
            )


        await self.client.say(embed=embed)






def setup(client):
    client.add_cog(Fun(client))
