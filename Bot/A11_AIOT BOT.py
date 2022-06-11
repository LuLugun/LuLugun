from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from flask.logging import create_logger
from linebot.models import MessageEvent,CarouselColumn,TextMessage,CarouselTemplate,MessageAction,ButtonsTemplate,TextSendMessage,StickerSendMessage,ImageSendMessage,TemplateSendMessage,PostbackTemplateAction,MessageTemplateAction
import pymysql
import os
import cv2
import pyimgur
import numpy as np
from detect_aiot import *
from data_to_jpg import *

def jpg_to_url(path):
    client_id = "d71e4a049aa4219"
    client_secret = '8205a0eedeaaed605421c765665f70294d39da9f'
    api = pyimgur.Imgur(client_id,client_secret)
    upload_image = api.upload_image(path)
    os.remove(path)
    return upload_image.link

def leave(filename):
    frame = cv2.imread(filename)
    lower_yellow = np.array([23,90,100]) # 綠色範圍低閾值
    upper_yellow = np.array([28,150,200]) # 綠色範圍高閾值
    hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask_yellow = cv2.inRange(hsv_img,lower_yellow,upper_yellow) # 根據顏色範圍刪選
    mask_yellow = cv2.medianBlur(mask_yellow,7) # 中值濾波
    contours,hierarchy = cv2.findContours(mask_yellow,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    num=0
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        if w*h > 1600:
            result_img = cv2.rectangle(frame,(x,y),(x + w,y + h),(0,255),2)
            num+=1
    
    os.remove(filename)
    path=filename

    cv2.imwrite(path,result_img)
    img_url = jpg_to_url(path)
    return img_url

def sql_connect(host,port,user,passwd,database):
    global db,cursor
    print('連線中....')
    print('host:%s\nuser:%s\npassword:********\ndatabase:%s\n'%(host,user,database))
    try:
        db=pymysql.connect(host=host,user=user,passwd=passwd,database=database,port = int(port))
        #os.system('cls')
        print('連線成功')
        cursor=db.cursor()
        return True
    except pymysql.Error as e:
        print("連線失敗:"+str(e))
        return False

def select_for_realtime(sql):
    cursor.execute(sql)
    result=cursor.fetchone()
    result = str(result[0]).strip('()')
    return result
    
app = Flask(__name__)
LOG = create_logger(app)
line_bot_api = LineBotApi('I4cfF7EAOgQa1g50LUr+hxXwgUwjSNdnd6sc7w6YeNEfZblDI9hfxfkego0Omzy2ajaAxAv0hzGOR/m+DuUeAUsVB57zLrU3azwiBc1b2oan/qP2e+iYhMtt+A4uTcX3XBgxFbukPUfBiPnEdVE5vQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('fbcce004ab7ebf3693d2909c87e4d9c6')



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
    
    user_id = event.source.user_id
    print("user_id =", user_id)
    print(event.message.type)
    if event.message.type == 'text':
        sql_connect('localhost',3306,'root','','aiot')
        stt = event.message.text
        if stt[0] =="圖" and stt[1] == "表":
            url = main(stt[2:])
            line_bot_api.reply_message(
                event.reply_token,
                ImageSendMessage(original_content_url=url,preview_image_url=url)
            )
        
        if stt == "溫度":
            sql='''SELECT `temperature` FROM `sensor_all` ORDER BY `time` DESC;'''
            line = select_for_realtime(sql)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = str(line)+'°C')
            )
        if stt == "濕度":
            sql='''SELECT `humidity` FROM `sensor_all` ORDER BY `time` DESC;'''
            line = select_for_realtime(sql)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = line+'%')
            )
        if stt == "亮度":
            sql='''SELECT `luminance` FROM `sensor_all` ORDER BY `time` DESC;'''
            line = select_for_realtime(sql)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = line)
            )
        if stt == "水溫":
            sql='''SELECT `Potted` FROM `sensor_all` ORDER BY `time` DESC;'''
            line = select_for_realtime(sql)
            sql='''SELECT `Reservoir` FROM `sensor_all` ORDER BY `time` DESC;'''
            line1 = select_for_realtime(sql)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = 'Potted:'+line+'°C'+" Reservoir:"+line1+'°C')
            )
        if stt == "CO2":
            sql='''SELECT `CO2` FROM `sensor_all` ORDER BY `time` DESC;'''
            line = select_for_realtime(sql)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = line)
            )
        if stt == "煙":
            sql='''SELECT `smoke` FROM `sensor_all` ORDER BY `time` DESC;'''
            line = select_for_realtime(sql)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = line)
            )
        if stt == "水質":
            sql='''SELECT `quality_Potted` FROM `sensor_all` ORDER BY `time` DESC;'''
            line = select_for_realtime(sql)
            sql='''SELECT `quality_Reservoir` FROM `sensor_all` ORDER BY `time` DESC;'''
            line1 = select_for_realtime(sql)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = 'Potted:'+line+' Reservoir:'+line1)
            )
        if stt == "抽水":
            sql = '''UPDATE `stop` SET `stop`='1' '''
            cursor.execute(sql)
            db.commit()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = "抽水 start")
            )
        if stt == "停止":
            sql = '''UPDATE `stop` SET `stop`='2' '''
            cursor.execute(sql)
            db.commit()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = "stop")
            )
        if stt == "加水":
            sql = '''UPDATE `stop` SET `stop`='3' '''
            cursor.execute(sql)
            db.commit()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = "加水 start")
            )
        if stt == "開燈":
            sql = '''UPDATE `action_always` SET `light`='1' '''
            cursor.execute(sql)
            db.commit()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = "開燈 start")
            )
        if stt == "換水":
            sql = '''UPDATE `action_always` SET `water`='1' '''
            cursor.execute(sql)
            db.commit()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = "換水 start")
            )
        if stt == "霧化器":
            sql = '''UPDATE `action_always` SET `humidification`='1' '''
            cursor.execute(sql)
            db.commit()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = "噴霧器 start")
            )
        if stt == "施肥":
            sql = '''UPDATE `action_always` SET `fertilizer`='1' '''
            cursor.execute(sql)
            db.commit()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = "施肥 start")
            )
        if stt =="中控台網頁":
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = "https://share.streamlit.io/lulugun/streamlit-example/streamlit_test.py")
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
        if stt == "折線圖":
            Carousel_template = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
            columns=[
                CarouselColumn(
                title='折線圖',
                text='溫室狀況',
                actions=[

                    MessageTemplateAction(
                        label="溫度",
                        text="圖表1平均 2021 12 溫度"
                    ),
                    MessageTemplateAction(
                        label="濕度",
                        text="圖表1平均 2021 12 濕度"
                    ),
                    MessageTemplateAction(
                        label="水溫",
                        text="圖表1平均 2021 12 水溫"
                    )
                    ]
                )
            ]
            )
            )
            line_bot_api.reply_message(event.reply_token,Carousel_template)
        if stt == "直方圖":
            Carousel_template = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
            columns=[
                CarouselColumn(
                title='直方圖',
                text='溫室狀況',
                actions=[

                    MessageTemplateAction(
                        label="溫度",
                        text="圖表3平均 2021 12 溫度"
                    ),
                    MessageTemplateAction(
                        label="濕度",
                        text="圖表3平均 2021 12 濕度"
                    ),
                    MessageTemplateAction(
                        label="水溫",
                        text="圖表3平均 2021 12 水溫"
                    )
                    ]
                )
            ]
            )
            )
            line_bot_api.reply_message(event.reply_token,Carousel_template)
        if stt == "點陣圖":
            Carousel_template = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
            columns=[
                CarouselColumn(
                title='點陣圖',
                text='溫室狀況',
                actions=[

                    MessageTemplateAction(
                        label="溫度",
                        text="圖表2平均 2021 12 溫度"
                    ),
                    MessageTemplateAction(
                        label="濕度",
                        text="圖表2平均 2021 12 濕度"
                    ),
                    MessageTemplateAction(
                        label="水溫",
                        text="圖表2平均 2021 12 水溫"
                    )
                    ]
                )
            ]
            )
            )
            line_bot_api.reply_message(event.reply_token,Carousel_template)
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
                        label="濕度",
                        text="濕度"
                    ),
                    MessageTemplateAction(
                        label="溫度",
                        text="溫度"
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
        db.close()
    
    if event.message.type=='image':
        image_content = line_bot_api.get_message_content(event.message.id)
        image_name = 'image_1.jpg'
        with open(image_name, 'wb') as fd:
            for chunk in image_content.iter_content():
                fd.write(chunk)
        url = model_detect(image_name)
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(original_content_url=url,preview_image_url=url)
        )

    
        
if __name__ == "__main__":        
    app.run()
