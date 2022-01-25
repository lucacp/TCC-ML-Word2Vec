#encoding: utf-8
import sys, codecs
import gensim, logging
from gensim.models import Word2Vec
from pprint import pprint
from sklearn.svm import SVC
import numpy as np
#from sklearn.multiclass import OneVsRestClassifier
#from sklearn.preprocessing import LabelBinarizer
#from sklearn.preprocessing import MultiLabelBinarizer
from tokenizacao import tokenize

def multDiv(txt,nmdt): #txt: nome_do_corpus ; nmdt: arquivo_das_respostas
    nmvc  = txt
    model = Word2Vec.load(nmvc)
    model.init_sims(replace = True)
    #pprint(model.wv.vocab)
    arq   = None
    try:
        arq    = codecs.open("treinamento"+nmvc+".txt",'r','utf-8')
    except FileNotFoundError:
        arq    = codecs.open("treinamento"+nmvc+".txt",'w','utf-8')
        pprint( model.wv.vocab , arq )
    arq.close()
    arq   = None
    #nmdt=str(sys.argv[2])
    arq   = codecs.open(nmdt,'r','utf-8')
    line  = arq.read()
    line  = tokenize(line)
    sp    = line.split('\n')
    arq.close()
    arq   = None
    arq   = codecs.open(nmvc+"-multdiv.txt",'w','ascii')
    num   = 0
    X     = []
    y     = []
    for line in sp:
        #print('Resposta '+str(num+1))
        num  = num+1
        mat  = None
        firs = 1
        linh = len(line.split())
        for one in line.split():
            if firs == 1:
                mat = model[one]
            else:
                try:
                    if firs < linh:
                        mat = mat * model[one]
                    else:
                        mat = mat / firs
                        y.append(int(one))
                except:
                    print(one+" linha: "+str(num))
            firs = firs+1
            #print(one)
            #print(model[one])
        #print('total')
        X.append(mat)
    arq.write(str(X)+"\n")
    arq1  = None
    arq1  = open("y.txt",'w+')
    arq1.write(str(y))
    arq1.close()
    arq1  = None
    arq.close()
    arq   = None

def multDivSw(txt,nmdt,sw): #txt: nome_do_corpus ; nmdt: arquivo_das_respostas ; sw: nome_arquivo_stopwords
    nmvc  = txt
    model = Word2Vec.load(nmvc)
    model.init_sims(replace=True)
    #pprint(model.wv.vocab)
    arq   = None
    try:
        arq    = codecs.open("treinamento"+nmvc+".txt",'r','utf-8')
    except FileNotFoundError:
        arq    = codecs.open("treinamento"+nmvc+".txt",'w','utf-8')
        pprint( model.wv.vocab , arq )
    arq.close()
    arq   = None
    
    arq   = codecs.open(sw,'r','utf-8')
    stp   = arq.read()
    arq.close()
    stp   = tokenize(stp)
    stw   = set(stp.split())
    arq   = None
    
    #nmdt=str(sys.argv[2])
    arq   = codecs.open(nmdt,'r','utf-8')
    line  = arq.read()
    line  = tokenize(line)
    sp    = line.split('\n')
    arq.close()
    arq   = None
    
    arq   = codecs.open(nmvc+"-multdiv-st.txt",'w','ascii')
    num   = 0
    X     = []
    y     = []
    for line in sp:
        #print('Resposta '+str(num+1))
        num  = num + 1
        mat  = None
        firs = 1
        fora = 0
        linh = len(line.split())
        for one in line.split():
            if one not in stw:
                try:
                    if firs == 1:
                        mat = model[one]
                    else:
                        if firs + fora < linh:
                            mat = mat * model[one]
                        else:
                            mat = mat / firs
                            y.append(int(one))
                    firs = firs+1
                except:
                    print(one+" linha: "+str(num))
            else:
                fora += 1
                #print("..."+one+"... stw: "+str(num))
            #firs = firs+1
            #print(one)
            #print(model[one])
        #print('total')
        X.append(mat)
    arq.write(  str(X) + "\n")
    arq.close()
    arq      =  None
    arq1     =  None
    arq1     =  open("y.txt",'w')
    arq1.write( str(y))
    arq1.close()
    arq1     =  None
    
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
ar    = None
ar    = open(str(sys.argv[1]))
dados =      str(sys.argv[2])
tex   = ar.read()
ar.close()
ar    = None
arqs  = tex.split('\n')
sw    =      str(sys.argv[3])
for i in arqs:
    print(i)
    multDiv(i,dados)
    multDivSw(i,dados,sw)
