from bs4 import BeautifulSoup
import urllib.request
save_list = []
f = open('GE2-3-output.csv', 'w', encoding='UTF-8')
for i in range(1,23):
    if i < 10:
        html_str = 'https://www.319papago.idv.tw/lifeinfo/sinyi/sinyi-0'+str(i)+'.html'
    else:
        html_str = 'https://www.319papago.idv.tw/lifeinfo/sinyi/sinyi-'+str(i)+'.html'
        content = urllib.request.urlopen(html_str)
        soup = BeautifulSoup(content, "lxml")
        element_list = soup.find_all('td',{'height':'33'})
        for n in element_list:
            name = n.contents[0]
            if name != '\xa0' and name != '信義房屋分店名稱' and  name != '暫無分店':
                print(name)
                save_list.append(name)
                if len(save_list) == 3:
                    f.write(save_list[0]+', '+save_list[1]+', '+save_list[2]+'\n')
                    save_list = []
f.close()