import os, sys
import codecs

limit = 200
linha = 0
ant   = 0
test  = 0
arqd1 = codecs.open("teste.txt",'w','utf-8')
arqd2 = codecs.open("train.txt",'w','utf-8')        
#with codecs.open("total.txt",'r','utf-8') as arq:
with codecs.open("aleatorio.txt",'r','utf-8') as arq:
    for line in arq:
        linha += 1
        #print(linha)
        if linha - ant == limit:
            arqd1.write(line)
            ant   = linha
            test += 1 
        else:
            arqd2.write(line)
            

print(linha-test)
print(test)
arqd1.close()
arqd2.close()
#25.706.090 linhas