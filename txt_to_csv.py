import numpy as np
import numpy as np
import pandas as pd
import re
summary=pd.DataFrame(['year','cited numbher','auther','journal','organ','Extension subject','subject','Extended keywords','keywords','country'])
data=['download_1-500.txt','download_501-1000.txt','download_1001-1500.txt','download_1501-2000.txt','download_2001-2141.txt']
#读取文件
for i in data:
    li = []
    with open('/Users/caofeizhen/Desktop/citespace/input/'+i,'r',encoding='utf8') as f:
        while True:
            cont = f.readline().replace('\n','')
            if not cont:  # 如果为空行,则表示取完一次数据,可以执行操作;
                if not li:  # 如果列表也为空,则表示数据读完了,结束循环
                    break
                try:#读取PY后的字段
                    PY = re.findall(r"\'PY\s([\w\W]*?)\'[A-Z][A-Z]", str(li))[0]
                except IndexError:
                    PY='no data'
                try:
                    TC = re.findall(r"\'TC\s([\w\W]*?)\'[A-Z][0-9]", str(li))[0]
                except IndexError:
                    TC='no data'
                try:
                    AF = re.findall(r"\'AF\s([\w\W]*?)\'[A-Z][A-Z]", str(li))[0]
                except IndexError:
                    AF='no data'
                try:
                    SO = re.findall(r"\'SO\s([\w\W]*?)\'[A-Z][A-Z]", str(li))[0]
                except IndexError:
                    SO='no data'
                try:
                    C1 = re.findall(r"\'C1\s([\w\W]*?)\'[A-Z][A-Z]", str(li))[0]
                except IndexError:
                    C1='no data'
                try:
                    WC = re.findall(r"\'WC\s([\w\W]*?)\'[A-Z][A-Z]", str(li))[0]
                except IndexError:
                    WC='no data'
                try:
                    SC = re.findall(r"\'SC\s([\w\W]*?)\'[A-Z][A-Z]", str(li))[0]
                except IndexError:
                    SC='no data'
                try:
                    ID = re.findall(r"\'ID\s([\w\W]*?)\"[A-Z][A-Z]|\'ID\s([\w\W]*?)\'[A-Z][A-Z]", str(li))[0][0]
                    if ID=='':
                        ID = re.findall(r"\'ID\s([\w\W]*?)\"[A-Z][A-Z]|\'ID\s([\w\W]*?)\'[A-Z][A-Z]", str(li))[0][1]
                except IndexError:
                    ID='no data'
                try:
                    DE = re.findall(r"\'DE\s([\w\W]*?)\'[A-Z][A-Z]", str(li))[0]
                except IndexError:
                    DE='no data'
                try:
                    RP = re.findall(r"\'RP\s([\w\W]*?)\'[A-Z][A-Z]", str(li))[0]
                except IndexError:
                    RP='no data'

                every = [PY,TC,AF,SO,C1,WC,SC,ID,DE,RP]
                every=pd.DataFrame(every)
                summary=pd.concat([summary,every],axis=1)
                li=[]
            else:
                li.append(cont)

#删减一些乱七八遭的字符使得看起来更整洁
summary=summary.applymap(lambda x: x.replace(";\',",';'))
summary=summary.applymap(lambda x: x.replace("\'",''))
summary.iloc[0]=summary.iloc[0].apply(lambda x: x.replace(",",''))
summary.iloc[1]=summary.iloc[1].apply(lambda x: x.replace(",",''))
summary.iloc[8]=summary.iloc[8].apply(lambda x: x.replace(',    ',' '))
summary.iloc[7]=summary.iloc[7].apply(lambda x: x.replace(',    ',' '))


summary.to_csv('/Users/caofeizhen/Desktop/merge.csv',header=False,index=False)#保存