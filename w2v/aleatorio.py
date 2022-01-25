import os, sys
import codecs
import random

linha = 0
ant   = 0
writ  = 0
limit = 15
arqd1 = codecs.open("aleatorio.txt",'w','utf-8')
with codecs.open("limitado.txt",'r','utf-8') as arq:
    for line in arq:
        #print(linha)
        #pal = len(line.split())
        linha += 1
        if linha - ant == limit:
            arqd1.write(line)
            writ += 1
            ant   = linha
            ran   = random.randint(0,100)
            if ran > 22:
                limit = 16
            else:
                limit = 15
#        
#
print(writ)
arqd1.close()
#15.792.127 linhas