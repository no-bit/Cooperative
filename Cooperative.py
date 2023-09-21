

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 05:34:26 2023

@author: Admin
"""

import pandas as pd
from datetime import *

listem = []
listem2 = []
with open('c.txt', 'r', encoding='UTF-8') as file:
    while (line := file.readline()):
        listem.append(line.rstrip())

dataframe1 = pd.read_excel('t.xlsx')

print(dataframe1.shape)
t2014 = pd.read_csv('2014.csv')
t2015 = pd.read_csv('2015.csv')
t2016 = pd.read_csv('2016.csv')
t2017 = pd.read_csv('2017.csv')
t2018 = pd.read_csv('2018.csv')
t2019 = pd.read_csv('2019.csv')
t2020 = pd.read_csv('2020.csv')
t2021 = pd.read_csv('2021.csv')
t2022 = pd.read_csv('2022.csv')

kapat=0
m=0
afk=0
dolar=0
total_dolar=0
error=0

for x in range(len(listem)):
    for col in dataframe1.columns[1:2]:
        for y in range(587):

            replaced = str(dataframe1[col][y]).replace('İ','i')
            replaced4 = (replaced).replace('I','ı')
            if (listem[x].lower() in replaced4.lower()):
                for col2 in dataframe1.columns[5:6]:

                    m+=int(dataframe1[col2][y])
                for col7 in dataframe1.columns[3:4]:
                    d1,m1,y1=[int(a) for a in str(dataframe1[col7][y]).replace('00:00:00','').split('-')]
                    b1=date(d1,m1,y1)

                    if (d1==2014):
                        for col8 in t2014.columns[0:1]:
                            if kapat==1:
                                break
                            for r in range(365):
                                if kapat==1:
                                    break
                                d2,m2,y2=[int(a) for a in str(t2014[col8][r]).replace('00:00:00','').split('.')]
                                b2=date(d2,m2,y2)
                                if (b2==b1):
                                    kapat=1
                                    for col9 in t2014.columns[1:2]:
                                        j=(t2014[col9][r].replace(',','.'))
                                        dolar+=int(dataframe1[col2][y])/float(j)

                    elif (d1==2015):
                        for col8 in t2015.columns[0:1]:
                            if kapat==1:
                                break
                            for r in range(261):
                                if kapat==1:
                                    break
                                d2,m2,y2=[int(a) for a in str(t2015[col8][r]).replace('00:00:00','').split('.')]
                                b2=date(y2,m2,d2)
                                if (b2==b1):
                                    kapat=1
                                    for col9 in t2015.columns[1:2]:
                                        j=(t2015[col9][r].replace(',','.'))
                                        dolar+=int(dataframe1[col2][y])/float(j)

                    elif (d1==2016):
                        for col8 in t2016.columns[0:1]:
                            if kapat==1:
                                break
                            for r in range(261):
                                if kapat==1:
                                    break
                                d2,m2,y2=[int(a) for a in str(t2016[col8][r]).replace('00:00:00','').split('.')]
                                b2=date(y2,m2,d2)
                          
                                if (b2==b1):
                                    kapat=1
                                    for col9 in t2016.columns[1:2]:
                                        j=(t2016[col9][r].replace(',','.'))
                                        dolar+=int(dataframe1[col2][y])/float(j)

                   
                    elif (d1==2017):
                        for col8 in t2017.columns[0:1]:
                            if kapat==1:
                                break
                            for r in range(260):
                                if kapat==1:
                                    break
                                d2,m2,y2=[int(a) for a in str(t2017[col8][r]).replace('00:00:00','').split('.')]
                                b2=date(y2,m2,d2)
                                if (b2==b1):    
                                    kapat=1
                                    for col9 in t2017.columns[1:2]:
                                        j=(t2017[col9][r].replace(',','.'))
                                        dolar+=int(dataframe1[col2][y])/float(j)

                    elif (d1==2018):
                        for col8 in t2018.columns[0:1]:
                            if kapat==1:
                                break
                            for r in range(261):
                                if kapat==1:
                                    break
                                d2,m2,y2=[int(a) for a in str(t2018[col8][r]).replace('00:00:00','').split('.')]
                                b2=date(y2,m2,d2)
                                if (b2==b1):
                                    kapat=1
                                    for col9 in t2018.columns[1:2]:
                                        j=(t2018[col9][r].replace(',','.'))
                                        dolar+=int(dataframe1[col2][y])/float(j)

                    elif (d1==2019):
                        for col8 in t2019.columns[0:1]:
                            if kapat==1:
                                break
                            for r in range(291):
                                if kapat==1:
                                    break
                                d2,m2,y2=[int(a) for a in str(t2019[col8][r]).replace('00:00:00','').split('.')]
                                b2=date(y2,m2,d2)
                                if (b2==b1):
                                    kapat=1
                                    for col9 in t2019.columns[1:2]:
                                        j=(t2019[col9][r].replace(',','.'))
                                        dolar+=int(dataframe1[col2][y])/float(j)

                    elif (d1==2020):
                        for col8 in t2020.columns[0:1]:
                            if kapat==1:
                                break
                            for r in range(523):
                                if kapat==1:
                                    break
                                d2,m2,y2=[int(a) for a in str(t2020[col8][r]).replace('00:00:00','').split('.')]
                                b2=date(y2,m2,d2)
                                if (b2==b1):
                                    kapat=1
                                    for col9 in t2020.columns[1:2]:
                                        j=(t2020[col9][r].replace(',','.'))
                                        dolar+=int(dataframe1[col2][y])/float(j)

                    elif (d1==2021):
                        for col8 in t2021.columns[0:1]:
                            if kapat==1:
                                break
                            for r in range(510):
                                if kapat==1:
                                    break
                                d2,m2,y2=[int(a) for a in str(t2021[col8][r]).replace('00:00:00','').split('.')]
                                b2=date(y2,m2,d2)
                                if (b2==b1):
                                    kapat=1
                                    for col9 in t2021.columns[1:2]:
                                        j=(t2021[col9][r].replace(',','.'))
                                        dolar+=int(dataframe1[col2][y])/float(j)
                                        kapat=1
                    elif (d1==2022):
                        for col8 in t2022.columns[0:1]:
                            if kapat==1:
                                break
                            for r in range(468):
                                if kapat==1:
                                    break
                                d2,m2,y2=[int(a) for a in str(t2022[col8][r]).replace('00:00:00','').split('.')]
                                b2=date(y2,m2,d2)
                                if (b2==b1):
                                    kapat=1
                                    for col9 in t2022.columns[1:2]:
                                        j=(t2022[col9][r].replace(',','.'))
                                        dolar+=int(dataframe1[col2][y])/float(j)
                                        
                    kapat=0                    
                                        
                                 


# =============================================================================
#     for col in dataframe2.columns[8:9]:
#         for a in range(1552):
#             replaced2 = str(dataframe2[col][a]).replace('İ','i')  
#             replaced3 = (replaced2).replace('I','ı') 
#             if (listem[x].lower() in replaced3.lower()):
#                 for col2 in dataframe2.columns[6:7]:
#                     m+=int(dataframe2[col2][a])
#                     for col7 in dataframe2.columns[0:1]:
#                         d1,m1,y1=[int(a) for a in str(dataframe2[col7][a]).replace('00:00:00','').split('-')]
#                         b1=date(d1,m1,y1)
#                         
#                        
#                         if (d1==2014):
#                             for col8 in t2014.columns[0:1]:
#                                 for r in range(365):
#                                     d2,m2,y2=[int(a) for a in str(t2014[col8][r]).replace('00:00:00','').split('.')]
#                                     b2=date(d2,m2,y2)
#                                     if (b2==b1):
#                                         for col9 in t2014.columns[1:2]:
#                                             j=(t2014[col9][r].replace(',','.'))
#                                             dolar+=int(dataframe2[col2][a])/float(j)
#                                 
#                         elif (d1==2015):
#                             for col8 in t2015.columns[0:1]:
#                                 for r in range(261):
#                                     d2,m2,y2=[int(a) for a in str(t2015[col8][r]).replace('00:00:00','').split('.')]
#                                     b2=date(y2,m2,d2)
#                                     if (b2==b1):
#                                         for col9 in t2015.columns[1:2]:
#                                             j=(t2015[col9][r].replace(',','.'))
#                                             dolar+=int(dataframe2[col2][a])/float(j)
#                             
#                         elif (d1==2016):
#                             for col8 in t2016.columns[0:1]:
#                                 for r in range(261):
#                                     d2,m2,y2=[int(a) for a in str(t2016[col8][r]).replace('00:00:00','').split('.')]
#                                     b2=date(y2,m2,d2)
#                                     if (b2==b1):
#                                         for col9 in t2016.columns[1:2]:
#                                             j=(t2016[col9][r].replace(',','.'))
#                                             dolar+=int(dataframe2[col2][a])/float(j)
#                        
#                         elif (d1==2017):
#                             for col8 in t2017.columns[0:1]:
#                                 for r in range(260):
#                                     d2,m2,y2=[int(a) for a in str(t2017[col8][r]).replace('00:00:00','').split('.')]
#                                     b2=date(y2,m2,d2)
#                                     if (b2==b1):    
#                                         for col9 in t2017.columns[1:2]:
#                                             j=(t2017[col9][r].replace(',','.'))
#                                             dolar+=int(dataframe2[col2][a])/float(j)
#                         
#                         elif (d1==2018):
#                             for col8 in t2018.columns[0:1]:
#                                 for r in range(261):
#                                     d2,m2,y2=[int(a) for a in str(t2018[col8][r]).replace('00:00:00','').split('.')]
#                                     b2=date(y2,m2,d2)
#                                     if (b2==b1):
#                                         for col9 in t2018.columns[1:2]:
#                                             j=(t2018[col9][r].replace(',','.'))
#                                             dolar+=int(dataframe2[col2][a])/float(j)
#                             
#                         elif (d1==2019):
#                             for col8 in t2019.columns[0:1]:
#                                 for r in range(291):
#                                     d2,m2,y2=[int(a) for a in str(t2019[col8][r]).replace('00:00:00','').split('.')]
#                                     b2=date(y2,m2,d2)
#                                     if (b2==b1):
#                                         for col9 in t2019.columns[1:2]:
#                                             j=(t2019[col9][r].replace(',','.'))
#                                             dolar+=int(dataframe2[col2][a])/float(j)
#                             
#                         elif (d1==2020):
#                             for col8 in t2020.columns[0:1]:
#                                 for r in range(523):
#                                     d2,m2,y2=[int(a) for a in str(t2020[col8][r]).replace('00:00:00','').split('.')]
#                                     b2=date(y2,m2,d2)
#                                     if (b2==b1):
#                                         for col9 in t2020.columns[1:2]:
#                                             j=(t2020[col9][r].replace(',','.'))
#                                             dolar+=int(dataframe2[col2][a])/float(j)
#                             
#                         elif (d1==2021):
#                             for col8 in t2021.columns[0:1]:
#                                 for r in range(510):
#                                     d2,m2,y2=[int(a) for a in str(t2021[col8][r]).replace('00:00:00','').split('.')]
#                                     b2=date(y2,m2,d2)
#                                     if (b2==b1):
#                                         for col9 in t2021.columns[1:2]:
#                                             j=(t2021[col9][r].replace(',','.'))
#                                             dolar+=int(dataframe2[col2][a])/float(j)
#                             
#                         elif (d1==2022):
#                             for col8 in t2022.columns[0:1]:
#                                 for r in range(468):
#                                     d2,m2,y2=[int(a) for a in str(t2022[col8][r]).replace('00:00:00','').split('.')]
#                                     b2=date(y2,m2,d2)
#                                     if (b2==b1):
#                                         for col9 in t2022.columns[1:2]:
#                                             j=(t2022[col9][r].replace(',','.'))
#                                             dolar+=int(dataframe2[col2][a])/float(j)
#                     
# =============================================================================

 

    
# =============================================================================
#     for col in dataframe3.columns[5:6]:
#         for c in range(160):
#             replaced5 = str(dataframe3[col][c]).replace('İ','i')
#             replaced6 = (replaced5).replace('I','ı')
#             if (listem[x].lower() in replaced6.lower()):
#                 for col3 in dataframe3.columns[2:3]:
#                     for col4 in dataframe3.columns[4:5]:  
#                         if (dataframe3[col4][c]>afk):
#                             m+=int (dataframe3[col3][c])
# =============================================================================



                       
                    
# =============================================================================
    print(listem[x],m,'tl')
    print(listem[x],dolar,'dolar')
    if (m>0 and dolar==0):
        error=1

    if(m==0):
        listem2.append(listem[x])
    m=0
    total_dolar+=dolar
    dolar=0
#     
print('toplam kişi sayısı:',len(listem))
print(total_dolar, 'total dolar rezervi')
print('bizim payimiz=', 134135.12992819145/total_dolar)
print(listem2, len(listem2))
# =============================================================================
    #text dosyamiza butun herkesi kucuk harfle ekle
if (error==1):
    print('error')
else:
    print('basarili')