# 中華民國交通部公路總局(交通資料庫)

## [VDLive.py](VDLive.py)

### 環境需求

python 3.6(或更高版本)

beautifulsoup4 >= 4.6.0

untangle >= 1.1.1

pandas >= 0.25.3

DateTime >= 4.3

urllib3 >= 1.26.7

### 架構介紹

由於希望可以實時的獲得公路總局最新的VD動態資料，所以本程式將透過實時的讀取[VD動態資料(1分鐘)](https://thbapp.thb.gov.tw/opendata/vd/one/VDLiveList.xml)將讀取到的內容傳換為csv

實時的讀取功能是透過網路爬蟲套件[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/)來讀取靜態的網頁內容，並以xml的檔案型態做儲存

讀取xml是透過[untangle](https://pypi.org/project/untangle/)來對xml進行解析，untangle.parse(filename)可讀取xml的檔案並將內容存成變數

csv的內容設計將只擷取一下欄位做紀錄
>* vdid
>* linkid
>* laneid
>* lanetype
>* speed
>* occupancy
>* vehicletype
>* volume
>* speed2
>* status
>* datacollecttime

## [xml_vdlive.py](xml_vdlive.py)

### 環境需求

python 3.6(或更高版本)

beautifulsoup4 >= 4.6.0

urllib3 >= 1.26.7

### 架構介紹

當[VDLive.py](VDLive.py)因為無法預期之原因執行出錯時，需要一個能夠回朔缺失未轉換成csv的xml原始檔

[xml_vdlive.py](xml_vdlive.py)該程式將透過網路爬蟲套件[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/)以一分鐘為周期將xml下載下來，並以下載時間命名

## [xml_to_csv_file.py](xml_to_csv_file.py)

### 環境需求

python 3.6(或更高版本)

pandas >= 0.25.3

untangle >= 1.1.1

### 架構介紹

[xml_to_csv_file.py](xml_to_csv_file.py)可批量的將xml轉換成csv

使用時輸入存放xml的資料夾的完整路徑，按下enter若csv的檔案名稱就代表正常運行，轉換成功的csv會在執行程式的資料夾內

若輸出出現不是csv的檔案名稱代表有檔案轉換失敗，程式會自動跳過該xml並輸出給使用者xml名稱

轉換失敗原因多半是xml為空的，原因是因為[xml_vdlive.py](xml_vdlive.py)在自動下載xml時會出現內容為空的狀況，但數量不多暫時以跳過處理