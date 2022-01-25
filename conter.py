import os, sys
import codecs

def Contador():
    linha = 0
    pala  = ''
    arqc  = codecs.open("counter.txt",'r','utf-8')
    line  = arqc.read()
    line  = line.replace("':",',')
    line  = line.replace("u'","")
    cnt   = {}
    for word in line.split(','):
        count = word
        if linha == 1:
            cnt[pala] = count
            linha = 0
        else:
            pala = word
            linha = 1
    arqc.close()
    arqc  = None
    return cnt
#