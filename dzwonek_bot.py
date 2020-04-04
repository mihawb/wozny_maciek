import asyncio
from random import choice
import discord
from discord.ext import commands
import time

ffmpeg_options = {
    'options': '-vn'
}

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dzwonek(self, ctx):
        h_start = time.gmtime(time.time())[3] + 2
        h_now = time.gmtime(time.time())[3] + 2

        '''#TIMER GODZINOWY
        while True:
            h_now = time.gmtime(time.time())[3] + 2
            if h_start + 1 == h_now:
                break
            time.sleep(1)
            print("Odliczanie (h) do dzwonka koncowego: " + str(time.gmtime(time.time())[3] + 1) + ":" + str(time.gmtime(time.time())[4]) + ":" + str(time.gmtime(time.time())[5]))
        '''
        #TIMER MINUTOWY
        while True:
            min_now = time.gmtime(time.time())[4]
            if min_now <= 2 and min_now >=0:
                break
            time.sleep(1)
            print("Odliczanie do dzwonka koncowego: " + str(time.gmtime(time.time())[3] + 2) + ":" + str(time.gmtime(time.time())[4]) + ":" + str(time.gmtime(time.time())[5])) 


        if ctx.voice_client is None:
            print("debug: sprawdzenie warunku ctx.voice_client is none poszlo")
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
                print("Polaczono z czatem glosowym.")
            else:
                await ctx.send("Nie znaleziono kanału głosowego.")
                print("wywolujacy nie byl podlaczony do czatu glosowego.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()
        
        time.sleep(3) # zeby dzwonek wybrzmial 

        dzwonki = ["krotki", "normalny", "dlugi"]
        query = f"C:/Users/mihaw/Desktop/cd_bot/dzwonek_{choice(dzwonki)}.mp3"
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query, executable="ffmpeg-win64-static/bin/ffmpeg.exe"))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send(f"Wybiła {h_now}:00! Czas na przerwę.")
        print("Dzwonek koncowy zadzwonil.")

        time.sleep(3) # zeby dzwonek wybrzmial 

        await ctx.voice_client.disconnect()

bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id}) from dzwonek_bot'.format(bot.user))
    print('------')

bot.add_cog(Music(bot))
bot.run('NjkyNDMzNTc3MjcwMzEzMDAx.XnueVQ.rg9wDpbNYjW7EqJcaUXm4SmjeyI')
