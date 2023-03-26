import re
with open('/data1/mzlv/csaData/DownloadData/RAPID_2019.de-en.xlf',mode='r') as fin:
    test = fin.read()
    en = re.findall('<target xml:lang=\"en\">(.*?)</target>',test)
    de = re.findall('<source xml:lang=\"de\">(.*?)</source>',test)
    print(type(en),type(de))
    print(len(en),len(de))
    enSet = set()
    deSet = set()
    for e,d in zip(en,de):
        #print(e,d)
        #print(key)
        #if len(e) > 80 or len(d) > 80:
        #   continue
        if len(e.split(' ')) > 80 or len(d.split(' ')) > 80:
            continue
        if e in enSet and d in deSet:
            continue
        enSet.add(e)
        deSet.add(d)
        with open('/data1/mzlv/csaData/processComplete/Original_train_datas/RAPID_2019.en','a') as fin_en:
            fin_en.write(e + '\n')
        with open('/data1/mzlv/csaData/processComplete/Original_train_datas/RAPID_2019.de','a') as fin_de:
            fin_de.write(d + '\n')
