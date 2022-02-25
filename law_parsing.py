import requests
from urllib.request import urlopen
import pandas as pd
import xml.etree.ElementTree as ET
from urllib.request import urlopen
import csv

law_data = pd.read_csv('C:\\Users\\hp\\법령검색목록+urls.csv')
f = open('law.csv', 'w', newline='', encoding='cp949')
wr = csv.writer(f)

for i in range(1291):

  url= "https://www.law.go.kr"
  link = law_data.loc[i]['법령상세링크']
  url += link
  response = urlopen(url).read()

  xtree = ET.fromstring(response)

  law_name = law_data.loc[i]['법령명']
  law_MST = law_data.loc[i]['법령MST']
  law_ID = law_data.loc[i]['법령ID']
  law_date = law_data.loc[i]['시행일자']
  law_num = law_data.loc[i]['공포번호']
  law_type = law_data.loc[i]['법령구분명']

  law_list = []
  temp = []

  temp.append(law_name)
  temp.append(law_MST)
  temp.append(law_ID)
  temp.append(law_date)
  temp.append(law_num)
  temp.append(law_type)
  temp2 = temp.copy()

  jomuns = xtree.find('조문')

  for jomun in jomuns:
    i = jomun.find('조문번호').text
    a = jomun.find('조문내용').text
    if jomun.find('항'):
      hangs = jomun.findall('항')
      for hang in hangs:
        if hang.find('항내용') is None:
          if hang.find('호'):
            hos = hang.findall('호')
            for ho in hos:
              if ho.find('호내용') is None:
                pass
              else:
                c = ho.find('호내용').text
                a += c
        else:
          b = hang.find('항내용').text
          a += b
          if hang.find('호'):
            hos = hang.findall('호')
            for ho in hos:
              if ho.find('호내용') is None:
                pass
              else:
                c = ho.find('호내용').text
                a += c
    temp2.append(i)
    temp2.append(a)
    try:
      wr.writerow(temp2)
    except:
      print(1)
    finally:
      temp2 = temp.copy()