#import pandas as pd
#import numpy as np
#df = pd.read_csv('/data1/mzlv/csaData/para.en-de-test.txt',error_bad_lines=False,header=None,sep = '\t')
#print(df.head())
#print(df.tail())
import re
enList = set()
deList = set()
file_write_en = open('/data1/mzlv/csaData/ParaCrawl.en.txt','w')
file_write_de = open('/data1/mzlv/csaData/ParaCrawl.de.txt','w')
for line in open('/data1/mzlv/csaData/ParaCrawl.en-de.txt'):
    #print(line)
    #de自带\n，en需要加上\n
    temp = line.split('\t')
    
    if len(temp) != 2:
        continue
    en,de = temp
    if en in enList or de in deList:
        continue
    enList.add(en)
    deList.add(de)

    file_write_en.writelines(en+'\n')
    file_write_de.writelines(de)
