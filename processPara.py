import re
enList = set()
deList = set()
file_write_en = open('/data1/mzlv/csaData/processComplete/Original_train_datas/ParaCrawl.en.txt','w')
file_write_de = open('/data1/mzlv/csaData/processComplete/Original_train_datas/ParaCrawl.de.txt','w')
for line in open('/data1/mzlv/csaData/DownloadData/ParaCrawl.en-de.txt'):
    #print(line)
    #de自带\n，en需要加上\n
    temp = line.split('\t')
    
    if len(temp) != 2:
        continue
    en,de = temp
    #if len(en) > 80 or len(de) > 80:
        #continue
    if len(en.split(' ')) > 80 or len(de.split(' ')) > 80:
        continue
    if en in enList and de in deList:
        continue
    enList.add(en)
    deList.add(de)

    file_write_en.writelines(en+'\n')
    file_write_de.writelines(de)
