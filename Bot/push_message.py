from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from flask.logging import create_logger
from linebot.models import MessageEvent,CarouselColumn,TextMessage,CarouselTemplate,MessageAction,ButtonsTemplate,TextSendMessage,StickerSendMessage,ImageSendMessage,TemplateSendMessage,PostbackTemplateAction,MessageTemplateAction
import Adafruit_DHT 
import serial
import time

line_bot_api = LineBotApi('Assertion Signing Key ')
yourID = 'Your user ID'
ser1 = serial.Serial('/dev/ttyACM0', 9600)
ser1.flush()

while True:
    try:
        ser1.write('t'.encode())
        line = ser1.readline().decode('utf-8').rstrip()
        if int(line) <= 165:
            list_file = 'documental_list.txt'
            documental_txt = open(list_file,"rt")
            documental_str = documental_txt.readline()
            documental_txt.close()
            documental_str = documental_str[:3]+'1'
            documental_txt = open(list_file,"w")
            documental_txt.write(documental_str)
            documental_txt.close()
            line_bot_api.push_message(yourID, 
                                TextSendMessage(text='該施肥了'))
        time.sleep(50)
        ser1.write('h'.encode())
        line = ser1.readline().decode('utf-8').rstrip()
        if int(line) <= 70.00:
            list_file = 'documental_list.txt'
            documental_txt = open(list_file,"rt")
            documental_str = documental_txt.readline()
            documental_txt.close()
            documental_str = documental_str[0]+'1'+documental_str[2:]
            documental_txt = open(list_file,"w")
            documental_txt.write(documental_str)
            documental_txt.close()
            line_bot_api.push_message(yourID, 
                                TextSendMessage(text='該加濕了'))
        time.sleep(550)
    except:
        pass
