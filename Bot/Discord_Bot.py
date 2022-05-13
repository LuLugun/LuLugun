import discord
import random
from discord.ext import commands
import time 
bot = commands.Bot(command_prefix='exe')
@bot.event
async def on_ready():
    print(">>嬌娃 is online<<")

@bot.event
async def on_member_join(member):
    if (member == ''''''):
        channel = bot.get_channel(574888963790077962)
        await channel.send("你的嬌娃已上線")
@bot.event
async def on_member_remove(member):
    if (member == '''首名#9624'''):
        channel = bot.get_channel(574888963790077962)
        await channel.send("暈船仔走瞜")

@bot.command()
async def 閃人(ctx):
    ss = discord.FFmpegPCMAudio(executable = '''C:\\Users\\User\\OneDrive\\桌面\\discord\\ffmpeg-N-100563-g66deab3a26-win64-gpl-shared-vulkan\\bin\\ffmpeg.exe''',source = '''C:\\Users\\User\\OneDrive\\桌面\\discord\\手淫bot\\SONG_8_210128.0227_2.mp3''')
    ctx.voice_client.play(ss)
    time.sleep(4)
    await ctx.voice_client.disconnect()

@bot.command()
async def 甲(ctx):
    ss = discord.FFmpegPCMAudio(executable = '''C:\\Users\\User\\OneDrive\\桌面\\discord\\ffmpeg-N-100563-g66deab3a26-win64-gpl-shared-vulkan\\bin\\ffmpeg.exe''',source = '''C:\\Users\\User\\OneDrive\\桌面\\discord\\手淫bot\\SONG_8_210128.0227_2.mp3''')
    ctx.voice_client.play(ss)
@bot.command()
async def 欸咦(ctx):
    ss = discord.FFmpegPCMAudio(executable = '''C:\\Users\\User\\OneDrive\\桌面\\discord\\手淫bot\\ffmpeg-N-100563-g66deab3a26-win64-gpl-shared-vulkan\\bin\\ffmpeg.exe''',source = '''C:\\Users\\User\\OneDrive\\桌面\\discord\\手淫bot\\_10076197.m4a''')
    ctx.voice_client.play(ss)
@bot.command()
async def 噁圖(ctx): 
    jpg = discord.File('''C:\\Users\\User\\OneDrive\\桌面\\discord\\bot\\S__101474308.jpg''')
    await ctx.send(file = jpg)
@bot.command()
async def 底迪(ctx):
    ss = discord.FFmpegPCMAudio(executable = '''C:\\Users\\User\\OneDrive\\桌面\\discord\\bot\\ffmpeg-N-100563-g66deab3a26-win64-gpl-shared-vulkan\\bin\\ffmpeg.exe''',source = '''C:\\Users\\User\\OneDrive\\桌面\\discord\\手淫bot\\voice_919529.aac''')
    ctx.voice_client.play(ss)
@bot.command()
async def 白(ctx):
    a = random.randrange(1,3)
    ss = discord.FFmpegPCMAudio(executable = '''C:\\Users\\User\\OneDrive\\桌面\\discord\\ffmpeg-N-100563-g66deab3a26-win64-gpl-shared-vulkan\\bin\\ffmpeg.exe''',source = '''C:\\Users\\User\\OneDrive\\桌面\\discord\\手淫bot\\抽語音\\'''+str(a)+'''.mp3''')
    ctx.voice_client.play(ss)



@bot.command()
async def 加入(ctx):
    #channel = bot.get_channel(667031692396986398)
    
    channel = ctx.author.voice.channel
    await channel.connect()

    ss = discord.FFmpegPCMAudio(executable = '''C:\\Users\\User\\OneDrive\\桌面\\discord\\bot\\ffmpeg-N-100563-g66deab3a26-win64-gpl-shared-vulkan\\bin\\ffmpeg.exe''',source = '''C:\\Users\\User\\OneDrive\\桌面\\discord\\手淫bot\\_10076197.m4a''')
    ctx.voice_client.play(ss)


@bot.event
async def on_voice_state_update(member,before,after):
    channel = bot.get_channel(574888963790077962)
    print(str(member))
    if(str(member) == ''''''):
        if (before.channel == None):
            await channel.send("嬌娃登場")
        if (before.channel != None):
            await channel.send("矮人酋長跑了")

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.errors.CommandNotFound):
        await ctx.send("哇挖!你打錯瞜")
    if isinstance(error,commands.errors.CommandInvokeError):
        await ctx.send("機器人八成沒進聊天室")
    else:
        await ctx.send("出事了")


bot.run('')


