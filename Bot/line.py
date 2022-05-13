from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from flask.logging import create_logger
from linebot.models import MessageEvent,CarouselColumn,TextMessage,CarouselTemplate,MessageAction,ButtonsTemplate,TextSendMessage,StickerSendMessage,ImageSendMessage,TemplateSendMessage,PostbackTemplateAction,MessageTemplateAction
import Adafruit_DHT 
import serial
from data_to_jpg import *

app = Flask(__name__)
LOG = create_logger(app)
line_bot_api = LineBotApi('Assertion Signing Key ')
handler = WebhookHandler('Channel secret ')
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4 

ser1 = serial.Serial('/dev/ttyACM0', 9600)
#ser2 = serial.Serial('/dev/ttyACM1', 9600)
ser1.flush()
#ser2.flush()



@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    LOG.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
    
@handler.add(MessageEvent)
def echo(event):
    print(event.message.type)
    if event.message.type == 'text':
        stt = event.message.text
        if stt[0] =="圖" and stt[1] == "表":
            url = main(stt[2:])
            line_bot_api.reply_message(
                event.reply_token,
                ImageSendMessage(original_content_url=url,preview_image_url=url)
            )
        if stt == "1號換水":
            ser1.write('z'.encode())
            list_file = 'documental_list.txt'
            documental_txt = open(list_file,"rt")
            documental_str = documental_txt.readline()
            documental_txt.close()
            documental_txt = open(list_file,"w")
            documental_str = '1'+documental_str[1:]
            documental_txt.write(documental_str)
            documental_txt.close()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = "1號換水 start")
            )
        """if stt == "2號換水":
            ser1.write('y'.encode())
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = "2號換水 start")
            )"""
        if stt == "1號抽水":
            ser1.write('a'.encode())
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = "1號抽水 start")
            )
        if stt == "1號加水":
            ser1.write('b'.encode())
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = "1號加水 start")
            )
        """if stt == "2號抽水":
            ser1.write('c'.encode())
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = "2號抽水 start")
            )
        if stt == "2號加水":
            ser1.write('d'.encode())
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = "2號加水 start")
            )"""
        if stt == "溫度":
            ser1.write('4'.encode())
            line = ser1.readline().decode('utf-8').rstrip()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = line)
            )
        if stt == "濕度":
            ser1.write('h'.encode())
            line = ser1.readline().decode('utf-8').rstrip()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = line)
            )
        if stt == "亮度":
            ser1.write('5'.encode())
            line = ser1.readline().decode('utf-8').rstrip()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = line)
            )
        if stt == "水溫":
            ser1.write('6'.encode())
            line = ser1.readline().decode('utf-8').rstrip()
            ser1.write('f'.encode())
            line1 = ser1.readline().decode('utf-8').rstrip()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = line+" "+line1)
            )
        if stt == "CO2":
            ser1.write('7'.encode())
            line = ser1.readline().decode('utf-8').rstrip()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = line)
            )
        if stt == "煙":
            ser1.write('8'.encode())
            line = ser1.readline().decode('utf-8').rstrip()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = line)
            )
        if stt == "水質":
            ser1.write('t'.encode())
            line = ser1.readline().decode('utf-8').rstrip()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = line)
            )
        """if stt == "水位":
            ser1.write('3'.encode())
            line = ser1.readline().decode('utf-8').rstrip()
            line1 = ser1.readline().decode('utf-8').rstrip()
            line2 = ser1.readline().decode('utf-8').rstrip()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = line+" "+line1+" "+line2)
            )"""
        if stt == "開燈":
            #ser2.write('9'.encode())
            list_file = 'documental_list.txt'
            documental_txt = open(list_file,"rt")
            documental_str = documental_txt.readline()
            documental_txt.close()
            documental_str = documental_str[:2]+'1'+documental_str[3]
            documental_txt = open(list_file,"w")
            documental_txt.write(documental_str)
            documental_txt.close()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = "開燈 start")
            )
        if stt == "換水":
            ser1.write('z'.encode())
            list_file = 'documental_list.txt'
            documental_txt = open(list_file,"rt")
            documental_str = documental_txt.readline()
            documental_txt.close()
            documental_txt = open(list_file,"w")
            documental_str = '1'+documental_str[1:]
            documental_txt.write(documental_str)
            documental_txt.close()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = "換水 start")
            )
        if stt == "噴霧器":
            #ser2.write('w'.encode())
            list_file = 'documental_list.txt'
            documental_txt = open(list_file,"rt")
            documental_str = documental_txt.readline()
            documental_txt.close()
            documental_str = documental_str[0]+'1'+documental_str[2:]
            documental_txt = open(list_file,"w")
            documental_txt.write(documental_str)
            documental_txt.close()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = "噴霧器 start")
            )
        if stt == "施肥":
            
            list_file = 'documental_list.txt'
            documental_txt = open(list_file,"rt")
            documental_str = documental_txt.readline()
            documental_txt.close()
            documental_str = documental_str[:3]+'1'
            documental_txt = open(list_file,"w")
            documental_txt.write(documental_str)
            documental_txt.close()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = "施肥 start")
            )
        """if stt =="監測報告":
            ser1.write('4'.encode())
            line = ser1.readline().decode('utf-8').rstrip()
            ser1.write('3'.encode())
            line = line+"\n"+ser1.readline().decode('utf-8').rstrip()+" "+ser1.readline().decode('utf-8').rstrip()+" "+ser1.readline().decode('utf-8').rstrip()
            ser1.write('6'.encode())
            line = line+"\n"+ser1.readline().decode('utf-8').rstrip()+" "+ser1.readline().decode('utf-8').rstrip()+" "+ser1.readline().decode('utf-8').rstrip()
            ser1.write('5'.encode())
            line = line+"\n"+ser1.readline().decode('utf-8').rstrip()
            
            ser1.write('7'.encode())
            line = line+"\n"+ser1.readline().decode('utf-8').rstrip()
            ser1.write('8'.encode())
            line = line+"\n"+ser1.readline().decode('utf-8').rstrip()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = line)
            )"""
            
        if stt == "停止":
            ser1.write('2'.encode())
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = "stop")
            )
        if stt == "感謝":
            line_bot_api.reply_message(
                event.reply_token,
                StickerSendMessage(package_id = '''11539''',sticker_id = '''52114110''')
            )
        if stt == "圖片":
            jpg_url = "https://cdn.discordapp.com/attachments/482516976497983490/805417339847049217/KAO_400x400.jpg"
            line_bot_api.reply_message(
                event.reply_token,
                ImageSendMessage(original_content_url = jpg_url,preview_image_url = jpg_url)
            )
        if stt == "溫室狀況":
            Carousel_template = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
            columns=[
                CarouselColumn(
                title='Menu',
                text='溫室狀況',
                actions=[

                    MessageTemplateAction(
                        label="亮度",
                        text="亮度"
                    ),
                    MessageTemplateAction(
                        label="水溫",
                        text="水溫"
                    ),
                    MessageTemplateAction(
                        label="溫濕度",
                        text="溫濕度"
                    )
                    ]
                )
            ]
            )
            )
            line_bot_api.reply_message(event.reply_token,Carousel_template)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = stt)
            )
    
    if event.message.type=='image':
        image_content = line_bot_api.get_message_content(event.message.id)
        image_name = 'image_1.jpg'
        with open(image_name, 'wb') as fd:
            for chunk in image_content.iter_content():
                fd.write(chunk)
        stt = str(leave(image_name))
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = stt)
        )


    
        
if __name__ == "__main__":
    
                           
    app.run()
