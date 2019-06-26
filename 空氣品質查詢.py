# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 20:02:42 2019

@author: Relieak
"""

import requests
import json 

url ="http://opendata.epa.gov.tw/webapi/Data/REWIQA/?$orderby=SiteName&$skip=0&$top=1000&format=json"
response = json.loads(requests.get(url,verify = False).text)

site = []
pm25 = []
aqi = []
status = []
time = []

for stat in response :
    
    site.append(stat["SiteName"])
    pm25.append(stat["PM2.5"])
    aqi.append(stat["AQI"])
    status.append(stat["Status"])
    time.append(stat["PublishTime"])
 
    
info = list(zip(pm25,aqi,status,time))     # 
data = dict(zip(site,info))

     
print("~~~~~歡迎進入空氣品質查詢系統~~~~~")
area = input("請輸入你要查詢的地區 ? ")
score = data.get(area,"無此地區資料")

if score != "無此地區資料" :
    print(""*2)
    print("地區 : %s\nPM2.5 : %s\nAQI : %s\n空氣品質 : %s\n觀測時間 : %s" %(area,score[0],score[1],score[2],score[3]))
    
    """ PM2.5 and AQI 用 %s 因為如果有時顯示 設備維護 是字串 用%d 會產生錯誤 ! """
else :
    print(""*2)
    print(score)


