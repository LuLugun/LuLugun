import discord
import random
from discord.ext import commands
import time 
bot = commands.Bot(command_prefix='馬保國')
@bot.event
async def on_ready():
    print(">>馬保國 上線啦<<")

@bot.command()
async def test(ctx,arg):
    await ctx.send(arg)

@bot.command()
async def ping(ctx):
    p = str(round(bot.latency*1000))+"ms"
    await ctx.send(p)

@bot.command()
async def 語音檔案(ctx,arg): 
    mp3 = discord.File('''C:\\Users\\User\\OneDrive\\桌面\\discord\\马保国语音包\\'''+arg+'''.mp3''')
    await ctx.send(file = mp3)
@bot.command()
async def 加入(ctx):
    #channel = bot.get_channel(667031692396986398)
    channel_str = bot.get_channel(804030941000892496)
    channel = ctx.author.voice.channel
    await channel.connect()
    await channel_str.send("朋友好")
@bot.command()
async def 閃人(ctx):
    ss = discord.FFmpegPCMAudio(executable = '''C:\\Users\\User\\OneDrive\\桌面\\discord\\ffmpeg-N-100563-g66deab3a26-win64-gpl-shared-vulkan\\bin\\ffmpeg.exe''',source = '''C:\\Users\\User\\OneDrive\\桌面\\discord\\马保国语音包\\谢谢朋友们.mp3''')
    ctx.voice_client.play(ss)
    time.sleep(2)
    await ctx.voice_client.disconnect()

@bot.command()
async def 請說(ctx,arg):
    ss = discord.FFmpegPCMAudio(executable = '''C:\\Users\\User\\OneDrive\\桌面\\discord\\ffmpeg-N-100563-g66deab3a26-win64-gpl-shared-vulkan\\bin\\ffmpeg.exe''',source = '''C:\\Users\\User\\OneDrive\\桌面\\discord\\马保国语音包\\'''+arg+'''.mp3''')
    ctx.voice_client.play(ss)

@bot.command()
async def 屁話(ctx):
    a = random.randrange(1,75)
    ss = discord.FFmpegPCMAudio(executable = '''C:\\Users\\User\\OneDrive\\桌面\\discord\\ffmpeg-N-100563-g66deab3a26-win64-gpl-shared-vulkan\\bin\\ffmpeg.exe''',source = '''C:\\Users\\User\\OneDrive\\桌面\\discord\\马保国语音包 - 複製\\'''+str(a)+'''.mp3''')
    ctx.voice_client.play(ss)


#@bot.event
#async def on_voice_state_update(member,before,after):
#    channel = bot.get_channel(791362434463563806)
#    #print(str(member)+str(before))
#    if(str(member) == '''馬保國本人#1670'''):
#        if (before.channel == None):
#            await channel.send("朋友好")
#        if (before.channel != None):
#            await channel.send("大意了啊")



bot.run('')
