from os import close
import discord
import random
from discord.ext import commands
import time 
from selenium import webdriver
import pyautogui

bot = commands.Bot(command_prefix='麥塊')

@bot.event
async def on_ready():
    print(">>嬌娃 is online<<")
    channel = bot.get_channel(574888963790077962)
    await channel.send("exe已上線")


@bot.command()
async def ip(ctx):
    driver = webdriver.Chrome()
    driver.get("https://www.whatismyip.com.tw/tw/")
    str_ip_element = driver.find_element_by_xpath("/html/body/b")
    str_ip = str_ip_element.get_attribute("textContent")
    driver.close()
    await ctx.send('今日ip:'+str_ip+':27051')

@bot.command()
async def re(ctx):
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.typewrite('java -Xmx15360M -Xms10240M -jar server.jar nogui')
    pyautogui.press('enter')
    await ctx.send('伺服器重啟中')

@bot.command()
async def start(ctx):
    pyautogui.typewrite('java -Xmx15360M -Xms10240M -jar server.jar nogui')
    pyautogui.press('enter')
    await ctx.send('伺服器啟動中')

bot.run('')



