

enSet = set()
deSet = set()
file_write_en = open('/data1/mzlv/csaData/europarl.en','w')
file_write_de = open('/data1/mzlv/csaData/europarl.de','w')
for line in open('/data1/mzlv/csaData/europarl-v10.de-en.tsv'):
    #print(line)
    #de自带\n，en需要加上\n
    temp = line.split('\t')
    
    de,en = temp[0],temp[1]
    if len(en) > 80 or len(de) > 80:
        continue
    if en in enSet or de in deSet:
        continue
    enSet.add(en)
    deSet.add(de)

    file_write_en.writelines(en+'\n')
    file_write_de.writelines(de+'\n')
