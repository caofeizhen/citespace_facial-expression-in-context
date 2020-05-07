import numpy as np
import pandas as pd
import re
summary=pd.read_csv('/Users/caofeizhen/Desktop/merge.csv',header=None)#读取由txt_csv处理得到的表格
summary.iloc[8]=summary.iloc[8].apply(lambda x: x.lower())
summary.iloc[7]=summary.iloc[7].apply(lambda x: x.lower())
summary.iloc[9]=summary.iloc[9].apply(lambda x: x.lower())


def select_keywords(names):#选择需要的关键字进行描述性统计
    hot = pd.DataFrame(index=[str(i) + ' ' for i in range(1991, 2020, 1)])
    for i in names:
        aa=summary.iloc[0][summary.iloc[8].str.contains(i)]
        aa=pd.DataFrame(aa).reset_index(drop=True);aa.columns=['year']
        zengke=pd.DataFrame(aa.groupby('year').size())
        hot=pd.concat([hot,zengke],axis=1,join='outer',sort=False)
    hot = hot.fillna(0)
    hot.columns =names
    all=pd.DataFrame(hot.iloc[0]).T
    for i in range(1,15,1):
        two_year=hot.iloc[2*i-1]+hot.iloc[2*i]
        all=all.append(two_year,ignore_index=True)
    all.index=['1991','1992-1993','1994-1995','1996-1997','1998-1999','2000-2001','2002-2003','2004-2005','2006-2007','2008-2009','2010-2011','2012-2013','2014-2015','2016-2017','2018-2019']
    return all.T


def select_auther(names):
    hot = pd.DataFrame(index=[str(i) + ' ' for i in range(1991, 2020, 1)])
    for i in names:
        aa=summary.iloc[0][summary.iloc[2].str.contains(i)]
        aa=pd.DataFrame(aa).reset_index(drop=True);aa.columns=['auther']
        zengke=pd.DataFrame(aa.groupby('auther').size())
        hot=pd.concat([hot,zengke],axis=1,join='outer',sort=False)
    hot = hot.fillna(0)
    hot.columns =names
    all=pd.DataFrame(hot.iloc[0]).T
    for i in range(1,15,1):
        two_year=hot.iloc[2*i-1]+hot.iloc[2*i]
        all=all.append(two_year,ignore_index=True)
    all.index=['1991','1992-1993','1994-1995','1996-1997','1998-1999','2000-2001','2002-2003','2004-2005','2006-2007','2008-2009','2010-2011','2012-2013','2014-2015','2016-2017','2018-2019']
    return all.T

def select_journal(names):
    hot = pd.DataFrame(index=[str(i) + ' ' for i in range(1991, 2020, 1)])
    for i in names:
        aa=summary.iloc[0][summary.iloc[3].str.contains(i)]
        aa=pd.DataFrame(aa).reset_index(drop=True);aa.columns=['journal']
        zengke=pd.DataFrame(aa.groupby('journal').size())
        hot=pd.concat([hot,zengke],axis=1,join='outer',sort=False)
    hot = hot.fillna(0)
    hot.columns =names
    all=pd.DataFrame(hot.iloc[0]).T
    for i in range(1,15,1):
        two_year=hot.iloc[2*i-1]+hot.iloc[2*i]
        all=all.append(two_year,ignore_index=True)
    all.index=['1991','1992-1993','1994-1995','1996-1997','1998-1999','2000-2001','2002-2003','2004-2005','2006-2007','2008-2009','2010-2011','2012-2013','2014-2015','2016-2017','2018-2019']
    return all.T

def select_organ(names):
    hot = pd.DataFrame(index=[str(i) + ' ' for i in range(1991, 2020, 1)])
    for i in names:
        aa=summary.iloc[0][summary.iloc[4].str.contains(i)]
        aa=pd.DataFrame(aa).reset_index(drop=True);aa.columns=['organ']
        zengke=pd.DataFrame(aa.groupby('organ').size())
        hot=pd.concat([hot,zengke],axis=1,join='outer',sort=False)
    hot = hot.fillna(0)
    hot.columns =names
    all=pd.DataFrame(hot.iloc[0]).T
    for i in range(1,15,1):
        two_year=hot.iloc[2*i-1]+hot.iloc[2*i]
        all=all.append(two_year,ignore_index=True)
    all.index=['1991','1992-1993','1994-1995','1996-1997','1998-1999','2000-2001','2002-2003','2004-2005','2006-2007','2008-2009','2010-2011','2012-2013','2014-2015','2016-2017','2018-2019']
    return all.T

def select_country(names):
    hot = pd.DataFrame(index=[str(i) + ' ' for i in range(1991, 2020, 1)])
    for i in names:
        aa=summary.iloc[0][summary.iloc[9].str.contains(i)]
        aa=pd.DataFrame(aa).reset_index(drop=True);aa.columns=['country']
        zengke=pd.DataFrame(aa.groupby('country').size())
        hot=pd.concat([hot,zengke],axis=1,join='outer',sort=False)
    hot = hot.fillna(0)
    hot.columns =names
    all=pd.DataFrame(hot.iloc[0]).T
    for i in range(1,15,1):
        two_year=hot.iloc[2*i-1]+hot.iloc[2*i]
        all=all.append(two_year,ignore_index=True)
    all.index=['1991','1992-1993','1994-1995','1996-1997','1998-1999','2000-2001','2002-2003','2004-2005','2006-2007','2008-2009','2010-2011','2012-2013','2014-2015','2016-2017','2018-2019']
    return all.T


hello=select_keywords(['emotion','facial expression','emotion recognition','facial expressions','context','fmri','social cognition','emotion perception','amygdala','schizophrenia','depression','emotion regulation','empathy',
                       'attention','erp','face processing'])
ssd=select_auther(['Hess, Ursula','de Gelder','Aviezer','Barrett','Matsumoto, David','Gendron, Maria','Ibanez, Agustin','Goubert, Liesbet','Pine, Daniel S','Neta, Maital'])
kkb=select_journal(['EMOTION','FRONTIERS IN PSYCHOLOGY','PLOS ONE','COGNITION & EMOTION','NEUROIMAGE','BIOLOGICAL PSYCHOLOGY','FRONTIERS IN HUMAN NEUROSCIENCE','JOURNAL OF NONVERBAL BEHAVIOR','NEUROPSYCHOLOGIA','SOCIAL COGNITIVE AND AFFECTIVE NEUROSCIENCE'])
kkp=select_organ(['UCL','Harvard Univ','Univ Amsterdam','Univ Geneva','Univ Pittsburgh','Univ Calif Los Angeles','Stanford Univ','Univ Calif Berkeley','Kings Coll London','McGill Univ'])
erp=select_keywords(['amygdala','n170','lpp','prefrontal cortex','orbitofrontal cortex','n400','temporal lobe'])
country=select_country(['usa','germany','england','canada','netherlands','peoples r china','australia','france','italy','japan'])

