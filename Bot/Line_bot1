from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from flask.logging import create_logger
from linebot.models import MessageEvent,CarouselColumn,TextMessage,CarouselTemplate,MessageAction,ButtonsTemplate,TextSendMessage,StickerSendMessage,ImageSendMessage,TemplateSendMessage,PostbackTemplateAction,MessageTemplateAction
import Adafruit_DHT 

app = Flask(__name__)
LOG = create_logger(app)
line_bot_api = LineBotApi('')
handler = WebhookHandler('')
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4 
import serial
ser1 = serial.Serial('/dev/ttyACM1', 9600)
ser2 = serial.Serial('/dev/ttyACM2', 9600)
ser1.flush()
ser2.flush()

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
    
@handler.add(MessageEvent,message = TextMessage)
def echo(event):
    stt = event.message.text
    if stt == "1號換水":
        ser1.write('z'.encode())
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = "1號換水 start")
        )
    if stt == "2號換水":
        ser1.write('y'.encode())
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = "2號換水 start")
        )
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
    if stt == "2號抽水":
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
        )
    if stt == "溫濕度":
        ser1.write('4'.encode())
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
        line1 = ser1.readline().decode('utf-8').rstrip()
        line2 = ser1.readline().decode('utf-8').rstrip()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = line+" "+line1+" "+line2)
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
    if stt == "水位":
        ser1.write('3'.encode())
        line = ser1.readline().decode('utf-8').rstrip()
        line1 = ser1.readline().decode('utf-8').rstrip()
        line2 = ser1.readline().decode('utf-8').rstrip()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = line+" "+line1+" "+line2)
        )
    if stt == "開燈":
        ser2.write('9'.encode())
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = "開燈 start")
        )
    if stt == "水質":
        ser2.write('t'.encode())
        line = ser2.readline().decode('utf-8').rstrip()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = line)
        )
    if stt == "換水":
        ser1.write('1'.encode())
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = "換水 start")
        )
    if stt =="監測報告":
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
        )
        
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

        
if __name__ == "__main__":
    app.run()
