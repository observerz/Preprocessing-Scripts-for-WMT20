enSet = set()
deSet = set()
file_write_en = open('/data1/mzlv/csaData/processComplete/Original_train_datas/WikiMatrix.en.txt','w')
file_write_de = open('/data1/mzlv/csaData/processComplete/Original_train_datas/WikiMatrix.de.txt','w')
for line in open('/data1/mzlv/csaData/DownloadData/WikiMatrix.v1.de-en.tsv'):
    #print(line)
    #de自带\n，en需要加上\n
    temp = line.split('\t')
    
    de,en = temp[1],temp[2]
    if len(en.split(' ')) > 80 or len(de.split(' ')) > 80:
        continue
    if en in enSet and de in deSet:
        continue
    enSet.add(en)
    deSet.add(de)

    file_write_en.writelines(en+'\n')
    file_write_de.writelines(de+'\n')
