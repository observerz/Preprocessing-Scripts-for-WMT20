import re
with open('/data1/mzlv/csaData/RAPID_2019.de-en.xlf',mode='r') as fin:
    test = fin.read()
    res = re.findall('<target xml:lang=\"en\">(.*?)</target>',test)
    for key in res:
        print(key)
        with open('/data1/mzlv/csaData/RAPID_2019.en','a') as fin:
            fin.write(key + '\n')