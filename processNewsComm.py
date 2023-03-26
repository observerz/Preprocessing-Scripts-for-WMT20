enSet = set()
deSet = set()
file_write_en = open('/data1/mzlv/csaData/processComplete/Original_train_datas/news-commentary-v15.en','w')
file_write_de = open('/data1/mzlv/csaData/processComplete/Original_train_datas/news-commentary-v15.de','w')
for line in open('/data1/mzlv/csaData/DownloadData/news-commentary-v15.de-en.tsv'):
    #print(line)
    #de自带\n，en需要加上\n
    temp = line.split('\t')
    
    de,en = temp
    #if len(en) > 80 or len(de) > 80:
    #    continue
    if len(en.split(' ')) > 80 or len(de.split(' ')) > 80:
        continue
    if en in enSet and de in deSet:
        continue
    enSet.add(en)
    deSet.add(de)

    file_write_en.writelines(en)
    file_write_de.writelines(de+'\n')
