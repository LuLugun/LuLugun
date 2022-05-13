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
    print(">>口嬌娃 is online<<")
    channel = bot.get_channel(574888963790077962)
    await channel.send("exe已上線")

@bot.event
async def on_member_join(member):
    if (member == '''首名#9624'''):
        channel = bot.get_channel(574888963790077962)
        await channel.send("你的口嬌娃已上線")
@bot.event
async def on_member_remove(member):
    if (member == '''首名#9624'''):
        channel = bot.get_channel(574888963790077962)
        await channel.send("暈船仔走瞜")

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
    time.sleep(5)
    pyautogui.typewrite('java -Xmx15360M -Xms10240M -jar server.jar')
    pyautogui.press('enter')
    await ctx.send('伺服器重啟中')

"""@bot.command()
async def 閃人(ctx):
    ss = discord.FFmpegPCMAudio(executable = '''ffmpeg''',source = '''/home/pi/Desktop/pi/discord_bot/手淫bot/SONG_8_210128.0227_2.mp3''')
    ctx.voice_client.play(ss)
    time.sleep(4)
    await ctx.voice_client.disconnect()

@bot.command()
async def 臭甲1(ctx):
    ss = discord.FFmpegPCMAudio(executable = '''ffmpeg''',source = '''/home/pi/Desktop/pi/discord_bot/手淫bot/SONG_8_210128.0227_2.mp3''')
    ctx.voice_client.play(ss)
@bot.command()
async def 臭甲2(ctx):
    ss = discord.FFmpegPCMAudio(executable = '''ffmpeg''',source = '''/home/pi/Desktop/pi/discord_bot/手淫bot/1617097836076.aac''')
    ctx.voice_client.play(ss)
@bot.command()
async def 欸咦(ctx):
    ss = discord.FFmpegPCMAudio(executable = '''ffmpeg''',source = '''/home/pi/Desktop/pi/discord_bot/手淫bot/_10076197.m4a''')
    ctx.voice_client.play(ss)
@bot.command()
async def 噁圖(ctx): 
    jpg = discord.File('''/home/pi/Desktop/pi/discord_bot/手淫bot/SPOILER_image0.jpg''')
    await ctx.send(file = jpg)
@bot.command()
async def 底迪(ctx):
    ss = discord.FFmpegPCMAudio(executable = '''ffmpeg''',source = '''/home/pi/Desktop/pi/discord_bot/手淫bot/voice_919529.aac''')
    ctx.voice_client.play(ss)
@bot.command()
async def 國動(ctx):
    a = random.randrange(1,6)
    ss = discord.FFmpegPCMAudio(executable = '''ffmpeg''',source = '''/home/pi/Desktop/pi/discord_bot/手淫bot/國動/'''+str(a)+'''.mp3''')
    ctx.voice_client.play(ss)

@bot.command()
async def 白爛(ctx):
    a = random.randrange(1,3)
    ss = discord.FFmpegPCMAudio(executable = '''ffmpeg''',source = '''/home/pi/Desktop/pi/discord_bot/手淫bot/抽語音/'''+str(a)+'''.mp3''')
    ctx.voice_client.play(ss)
@bot.command()
async def 塔羅牌_1(ctx):
    while True:
        a1 = random.randint(0, 75)
        a2 = random.randint(0, 75)
        a3 = random.randint(0, 75)
        if a1 != a2 and a1 != a3 and a2 != a3:
            #Tarot_str = "過去:"+Tarot_list[a1]+"\n"+"現在:"+Tarot_list[a2]+"\n"+"未來:"+Tarot_list[a3]
            break
        else:
            pass
    #print(Tarot_str)
    jpg1 = discord.File('''/home/pi/Desktop/pi/discord_bot/手淫bot/塔羅牌/'''+str(a1)+'''.jpg''')
    jpg2 = discord.File('''/home/pi/Desktop/pi/discord_bot/手淫bot/塔羅牌/'''+str(a2)+'''.jpg''')
    jpg3 = discord.File('''/home/pi/Desktop/pi/discord_bot/手淫bot/塔羅牌/'''+str(a3)+'''.jpg''')
    
    channel = bot.get_channel(574888963790077962)
    await channel.send(file = jpg1)
    await channel.send(file = jpg2)
    await channel.send(file = jpg3)
    



@bot.command()
async def 加入(ctx):
    #channel = bot.get_channel(667031692396986398)
    
    channel = ctx.author.voice.channel
    await channel.connect()

    ss = discord.FFmpegPCMAudio(executable = '''ffmpeg''',source = '''/home/pi/Desktop/pi/discord_bot/手淫bot/_10076197.m4a''')
    ctx.voice_client.play(ss)


@bot.event
async def on_voice_state_update(member,before,after):
    channel = bot.get_channel(574888963790077962)
    #print(str(member))
    if(str(member) == '''首名#9624'''):
        if (before.channel == None):
            await channel.send("口嬌娃登場")
        if (before.channel != None):
            await channel.send("矮人酋長跑了")"""


bot.run('')



