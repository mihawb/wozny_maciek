import discord
import time
from random import choice
from discord.ext import commands

bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id}) from wozny_bot'.format(bot.user))
    print('------')

@bot.command()
async def pomoc(ctx):
    lista = "Lista obowiązków woźniego:\n" + "!dzwonek - uruchamia dzwonek, który zadzwoni na koniec lekcji\n" + "!play <ścieżka> - odtwarza plik audio z komputera wywołującego\n" + "!stream <link> - odtwarza audio z filmiku z youtube\n" + "!volume <liczba 0-100> - zmiana głośności odtwarzania\n" + "!stop - zatrzymuje odtwarzanie\n" + "!losowanie - wybiera losowego ucznia z klasy\n" + "!listopad - karta pułapka\n" + "!widac - no przecież to widać\n" + "!salut - na zdrowie!"
    await ctx.send(lista)

@bot.command()
async def listopad(ctx):
    await ctx.send("Karol Kuźniak zamknij mordę")

@bot.command()
async def won(ctx):
    await ctx.send("Dzie tu łazisz! Dopiero myłem, mokre jeszcze!")

@bot.command()
async def losowanie(ctx):
    await ctx.send("Maszyna losująca jest pusta, następuje zwolnienie blokady...")
    time.sleep(2)
    await ctx.send("*szuru szuru szuru*")
    time.sleep(3)
    await ctx.send("Numer 13!")

@bot.command()
async def salut(ctx):
    salut =['Gdy cesarz Napoleon w potyczce zażywa\nRaz po raz, to znak pewny, że bitwę wygrywa!',
            '"Księże Robaku", mówił, "Księże Bernardynie,\nObaczymy się w Litwie, może nim rok minie;\nPowiedz Litwinom, niech mię czekają z tabaką\nCzęstochowską, nie biorę innej, tylko taką."',
            'Milczało chwilę; potem na pół ciche słowa\nPowtarzano: "Tabaka z Polski? Częstochowa?\nDąbrowski? z ziemi włoskiej?" - aż na koniec razem,\nJakby myśl z myślą, wyraz sam zbiegł się z wyrazem,\nWszyscy jednogłośnie, jak na dane hasło,\nKrzyknęli: "Dąbrowskiego! "']
    await ctx.send(choice(salut))

@bot.command()
async def widac(ctx):
    await ctx.send("Toż to nawet ja widzę, kurde.")

@bot.command()
async def matura(ctx):
    await ctx.send(f"Do matury pozostało {int((1588575600 - int(time.time())) / 86400)} dni.")

bot.run("TOKEN")
