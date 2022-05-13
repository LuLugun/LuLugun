from pymysql.err import IntegrityError
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymysql
import os
from selenium.common.exceptions import TimeoutException ,InvalidArgumentException
import itertools
from selenium.webdriver.chrome.options import Options

chromeoptions = Options()
chromeoptions.add_argument("--log-level=3")

#seting

links_parsed_count = 0
links_parsed_count_tag = 0
url_list = []
email = 'aep.stevenl.test1'
password = '*7777xxxx'
#login
def login(chrome_driver,email,password):
    chrome_driver.get("https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dzh-TW%26next%3D%252F&hl=zh-TW&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    Web_Driver_Wait(chrome_driver,'//*[@id="identifierNext"]/div/button')
    email_input = chrome_driver.find_element_by_xpath('//*[@id="identifierId"]')
    email_input.send_keys(email)
    button = chrome_driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
    button.click()
    Web_Driver_Wait(chrome_driver,'//*[@id="passwordNext"]/div/button')
    time.sleep(1)
    password_input = chrome_driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    password_input.send_keys(password)
    button = chrome_driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
    button.click()
#search
def input_Keyword_search(chrome_driver,Keyword):
    Keyword_input = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
    Keyword_input.send_keys(Keyword)
    search_button = chrome_driver.find_element_by_id("search-icon-legacy")
    search_button.click()
    
def Web_Driver_Wait(chrome_driver,str_xpath):
    while True:
        try:
            element = WebDriverWait(chrome_driver,10,0.5).until(
                EC.presence_of_element_located((By.XPATH,str_xpath))
            )
        except:
            print("loding")
        else:
            break

def get_title_href(chrome_driver,Keyword,video_confirm_list,elements_id):
    global links_parsed_count
    links = chrome_driver.find_elements_by_id(elements_id)
    for link in links[links_parsed_count:]:
        partial_href = link.get_attribute("href")
        partial_title = link.get_attribute("title")

        if str(partial_href) not in video_confirm_list and str(partial_href) != "None":
            video_confirm_list.append(str(partial_href))
            input_SQL(str(partial_href),partial_title,Keyword)

    links_parsed_count = len(links)
    return video_confirm_list
        
def swipe_page(chrome_driver,times_record):
    js = 'var q=document.documentElement.scrollTop='+str(100000*times_record)
    chrome_driver.execute_script(js)
    confirm = chrome_driver.find_element_by_id("message")
    partial_confirm = confirm.get_attribute("class")
    if partial_confirm != None:
        return "End"

def sql_connect():
    global db,cursor,host
    host='10.110.219.192'
    user='intern'
    passwd='Abcd@4321'
    database='intern_creatable'
    print('連線中....')
    print('host:%s\nuser:%s\npassword:********\ndatabase:%s\n'%(host,user,database))
    try:
        db=pymysql.connect(host=host,user=user,passwd=passwd,database=database)
        os.system('cls')
        print('連線成功')
        cursor=db.cursor()
        return True
    except pymysql.Error as e:
        print("連線失敗:"+str(e))
        return False

def input_SQL(herf,title,keyword):
    sql='''INSERT INTO `yt_crawler_keyword_search` ( `youtube_url`,`youtube_title`, `keyword`) VALUES ('%s','%s','%s')'''%(herf,title.replace('\'','\\\''),keyword)
    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.Error as e:
        if str(e)[:5] == '(1062':  #db已存在過一樣的紀錄
            if keyword[:5] == 'https':  #來自推薦影片
                pass
            else:  #來自關鍵字搜尋
                sql = """SELECT keyword FROM `yt_crawler_keyword_search`WHERE youtube_url = '%s';"""%(herf)
                cursor.execute(sql)
                result=cursor.fetchone()
                result = str(result).strip('()')
                str_keyword = result+str(keyword)
                if str_keyword[:6] == "'https" or str_keyword[:4] == 'None':  #更新欄位keyword 將推薦影片來源替換成關鍵字
                    sql="""UPDATE `yt_crawler_keyword_search` SET `keyword`= '%s' WHERE `youtube_url` = '%s';"""%(keyword,herf)
                else:  #更新欄位keyword 將新的關鍵字加入原有的關鍵字清單裡
                    sql="""UPDATE `yt_crawler_keyword_search` SET `keyword`= '%s' WHERE `youtube_url` = '%s';"""%(str_keyword,herf)
                cursor.execute(sql)
                db.commit()
        else:
            print(e)
            print(herf,title)
        
        pass

def step2(chrome_driver,url):
    chrome_driver.get(url)
    Web_Driver_Wait(chrome_driver,'//*[@id="text"]/a')
    herf_list = []
    title_list = []
    try:
        str_channel_tag = None
        channel = chrome_driver.find_element_by_xpath('//*[@id="text"]/a')
        str_channel = channel.get_attribute("textContent")
        introduce = chrome_driver.find_element_by_xpath('//*[@id="description"]/yt-formatted-string')
        str_introduce = introduce.get_attribute("textContent")
        str_introduce = str(str_introduce).replace('"',"")
        tag_number = 1
        try:
            channel_tag = chrome_driver.find_element_by_xpath('//*[@id="container"]/yt-formatted-string/a['+str(tag_number)+']')
            str_channel_tag = channel_tag.get_attribute("textContent")
        except:
            pass
        while True:
            try:
                tag_number = tag_number + 1
                channel_tag = chrome_driver.find_element_by_xpath('//*[@id="container"]/yt-formatted-string/a['+str(tag_number)+']')
                str_channel_tag = str_channel_tag+','+channel_tag.get_attribute("textContent")
            except:
                break
        step2_update_SQL(url,str_channel,str_introduce,str_channel_tag)
        
        video_renderer = chrome_driver.find_elements_by_xpath('//*[@id="dismissible"]/div/div[1]/a')
        for link in video_renderer:
            herf = link.get_attribute("href")
            herf_list.append(herf)
        video_title = chrome_driver.find_elements_by_id('video-title')
        for link in video_title:
            title = link.get_attribute("title")
            title_list.append(title)
        counter_a = 0
        for i in herf_list:
            input_SQL(herf_list[counter_a],title_list[counter_a],url)
            counter_a = counter_a + 1
    except:
        print('not in db',str_channel,str_introduce,str_channel_tag)
        pass

def step2_update_SQL(url,str_channel,str_introduce,str_channel_tag):
    sql='''UPDATE `yt_crawler_keyword_search` SET  `youtube_channel` = """%s""" , `youtube_introduce` = """%s""", `youtube_tag` = "%s" WHERE `youtube_url` = "%s";'''%(str_channel,str_introduce,str_channel_tag,url)
    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.Error as e:
        print(e)
        print(sql)
        pass

def step3_get_tag():
    sql = '''SELECT `youtube_tag` FROM `yt_crawler_keyword_search` WHERE youtube_tag IS NOT NULL AND youtube_tag != 'None';'''
    cursor.execute(sql)
    result=cursor.fetchall()
    result=list(result)
    ALL_Tag = []
    result = [x[0].replace('#','').replace('\'', '').split(',') for x in result]
    ALL_Tag = list(set(itertools.chain(*result)))
    return ALL_Tag

def step3_get_title_href(chrome_driver,tag,elements_id):
    video_confirm_list = []
    global links_parsed_count_tag
    links = chrome_driver.find_elements_by_id(elements_id)
    for link in links:
        partial_href = link.get_attribute("href")
        partial_title = link.get_attribute("title")

        if str(partial_href) not in video_confirm_list and str(partial_href) != "None":
            video_confirm_list.append(str(partial_href))
            input_SQL_tag(str(partial_href),partial_title,tag)

    links_parsed_count_tag = len(links)

def input_SQL_tag(herf,title,tag):
    sql='''INSERT INTO `yt_crawler_keyword_search` ( `youtube_url`,`youtube_title`, `youtube_tag`) VALUES ('%s','%s','%s')'''%(herf,title.replace('\'','\\\''),tag)
    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.Error as e:
        if str(e)[:5] == '(1062':  #db已存在過一樣的紀錄
            pass
        else:
            print(e)

def step4_get_channel():
    sql = '''SELECT `youtube_channel` FROM `yt_crawler_keyword_search` WHERE youtube_channel IS NOT NULL;'''
    cursor.execute(sql)
    result=cursor.fetchall()
    ALL_channel = list(set([str(x[0]).strip('()').replace('\'','') for x in result]))
    return ALL_channel

def step4_get_channel_playlist(driver,channel):
    sql = '''SELECT `youtube_url` FROM `yt_crawler_keyword_search` WHERE youtube_channel = '%s';'''%(channel)  #在DB尋找一部對應頻道的影片URL
    try:
        cursor.execute(sql)
        result=cursor.fetchone()
        result = str(result[0]).strip('()').replace('\'','')
        try:
            #開啟影片url
            driver.get(result)
        except TimeoutException as exception:
            driver.close()
            driver = webdriver.Chrome(chrome_options = chromeoptions)
            login(driver,email,password)
            driver.get(result)
        except:
            print(channel,':',result)
            return None
        time.sleep(2)
        try:
            #嘗試定位影片中間是否有出現提示字幕，若有出現代表該影片不能使用
            reason = driver.find_element_by_xpath('//*[@id="reason"]')  
            message = reason.get_attribute("textContent")
            print(result)
        except:
            #定位元素失敗代表影片正常可以使用
            Web_Driver_Wait(driver,'//*[@id="top-row"]/ytd-video-owner-renderer/a')
            #透過取得影片頁面裡的頻道連結加上'/playlists'即可得到頻道的播放清單連結
            link = driver.find_element_by_xpath('//*[@id="top-row"]/ytd-video-owner-renderer/a')
            partial_href = link.get_attribute("href")
            partial_href = partial_href+'/playlists'
            try:
                driver.get(partial_href)
            except TimeoutException as exception:
                driver.close()
                driver = webdriver.Chrome(chrome_options = chromeoptions)
                login(driver,email,password)
                driver.get(partial_href)
            Web_Driver_Wait(driver,'//*[@id="tabsContent"]/tp-yt-paper-tab[3]')
            links = driver.find_elements_by_id('video-title')
            for link in links:
                partial_href = link.get_attribute("href")
                partial_title = link.get_attribute("title")
                #print(partial_href,partial_title)
                sql='''INSERT INTO `yt_crawler_play_list` ( `yt_list_url`,`channel`, `list_title`) VALUES ('%s','%s','%s')'''%(partial_href,channel,partial_title.replace('\'','\\\''))
                try:
                    cursor.execute(sql)
                    db.commit()
                except pymysql.Error as e:
                    if str(e)[:5] == '(1062':
                        pass
                except:
                    print(sql)
                    pass
    except:
        pass

def step5_get_playlist():
    sql = """SELECT yt_list_url FROM `yt_crawler_play_list`;"""
    cursor.execute(sql)
    result=cursor.fetchall()
    ALL_Play_list = list(set([str(x[0]).strip('()').replace('\'','') for x in result]))
    return ALL_Play_list

def step5_playlist_get_url(driver,platlist):
    try:
        try:
            driver.get(platlist)
        except TimeoutException as exception:
            driver.close()
            driver = webdriver.Chrome(chrome_options = chromeoptions)
            login(driver,email,password)
            driver.get(platlist)
        Web_Driver_Wait(driver,'//*[@id="text"]/a')
        try:
            links = driver.find_elements_by_id('wc-endpoint')
            i = 1
            for link in links:
                title_xpath = '//ytd-playlist-panel-video-renderer[%s]/a/div/div[3]/h4/span'%(str(i))
                title = driver.find_element_by_xpath(title_xpath)
                partial_href = link.get_attribute("href")
                partial_title = title.get_attribute("title")
                sql='''INSERT INTO `yt_crawler_keyword_search` ( `youtube_url`,`youtube_title`) VALUES ('%s','%s')'''%(str(partial_href),str(partial_title).replace('\'','\\\''))
                try:
                    cursor.execute(sql)
                    db.commit()
                except pymysql.Error as e:
                    if str(e)[:5] == '(1062':  #db已存在過一樣的紀錄
                        pass
                    else:
                        print(e)
                i = i+1           
        except:
            pass
    except:
        pass           


if __name__ == '__main__':
    sql_connect()
    driver = webdriver.Chrome(chrome_options = chromeoptions)
    login(driver,email,password)
    while True:
        Web_Driver_Wait(driver,'/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
        print('(1)step1\n(2)step2\n(3)step3\n(4)step4\n(5)step5')
        Menu_options=input('請輸入選單選項:')
        os.system('cls')
        if Menu_options=='1':
            Keyword = input("輸入關鍵字:")
            links_parsed_count = 0
            input_Keyword_search(driver,Keyword)
            Web_Driver_Wait(driver,"//*[@id='button']")
            times_record = 0
            video_confirm_list = []
            while True:
                video_confirm_list = get_title_href(driver,Keyword,video_confirm_list,"video-title")
                times_record = times_record + 1
                if swipe_page(driver,times_record) == "End":
                    break
                

        elif Menu_options=='2':
            sql = """SELECT youtube_url FROM `yt_crawler_keyword_search`WHERE youtube_channel IS NULL and keyword not LIKE 'http%';"""
            cursor.execute(sql)
            result=cursor.fetchall()
            result=list(result)
            for i in result:
                url = str(i).strip('()')
                url = url[:-1]
                url = url.strip("'")
                try:
                    step2(driver,url)
                except TimeoutException as exception:  #Chromedriver載入超時例外處理
                    driver.close()
                    driver = webdriver.Chrome(chrome_options = chromeoptions)
                    login(driver,email,password)
                    step2(driver,url)

        elif Menu_options=='3':
            ALL_Tag = step3_get_tag()
            url = 'https://www.youtube.com/hashtag/'
            for i in ALL_Tag:
                try:
                    driver.get(url+i)
                except TimeoutException as exception:  #Chromedriver載入超時例外處理
                    driver.close()
                    driver = webdriver.Chrome(chrome_options = chromeoptions)
                    login(driver,email,password)
                    driver.get(url+i)
                Web_Driver_Wait(driver,'//*[@id="header"]')
                step3_get_title_href(driver,'#'+i,"video-title-link")

        elif Menu_options=='4':
            ALL_channel = step4_get_channel()
            for channel in ALL_channel:
                step4_get_channel_playlist(driver,channel)

        elif Menu_options=='5':
            ALL_Play_list = step5_get_playlist()
            for playlist in ALL_Play_list:
                step5_playlist_get_url(driver,playlist)
        else:
            break
        
    driver.close()    
    db.close()        
    
