import os, sys
import codecs
from tokenizacao import tokenize
from collections import Counter
cnt = Counter()
linha = 0
#limit = 35
arqd1 = codecs.open("counter.txt",'w','utf-8')
with codecs.open("total.txt",'r','utf-8') as arq:
    for line in arq:
        #print(linha)
        line = tokenize(line)
        for word in line.split():
            cnt[word] += 1
            linha     += 1
        #if pal <= limit: #21.213.214
            #linha += 1
            #arqd1.write(line)
#        if pal <= limit and pal > 0: #15.792.127 #tokenizado 15.769.737
#            linha += 1
#            arqd1.write(line)
#
arqd1.write(str(cnt))
print(linha)#counter 482.688.013
arqd1.close()
#25.706.090 linhas