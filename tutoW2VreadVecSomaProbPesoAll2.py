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
#from conter import Contador

def somaProbp(txt,nmdt): #txt: nome_do_corpus ; nmdt: arquivo_das_respostas
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
    numlin = np.int32(len(model.wv.vocab))
#    print(numlin)
    arq   = None
    #nmdt=str(sys.argv[2])
    arq   = codecs.open(nmdt,'r','utf-8')
    line  = arq.read()
    line  = tokenize(line)
    sp    = line.split('\n')
    arq.close()
    arq   = None
    arq1  = codecs.open(nmvc+"-2-peso1.txt",'w','ascii')
    arq2  = codecs.open(nmvc+"-2-peso2.txt",'w','ascii')
    num   = 0
    X1    = []
    X2    = []
    y     = []
    
    linha = 0
    pala  = ''
    arqc  = codecs.open("counter.txt",'r','utf-8')
    liine  = arqc.read()
    liine  = liine.replace(" ","")
    liine  = liine.replace("':",',')
    liine  = liine.replace("u'","")
    cnt   = {}
    for word in liine.split(','):
        count = word
        if linha == 1:
            cnt[pala] = count
            linha = 0
        else:
            pala = word
            linha = 1
    arqc.close()
    arqc  = None
    
    for line in sp:
        #print('Resposta '+str(num+1))
        num  = num+1
        mat1  = None
        mat2  = None
        firs = 1
        linh = len(line.split())
        a1   = np.float32(0.001)
        a2   = np.float32(0.0001)
        for one in line.split():
            prob = np.int32(cnt[one])/numlin
            A1   = a1/(a1 + prob)
            A2   = a2/(a2 + prob)
            #print(A1)
            #print(A2)
            if firs == 1:
                #print(cnt[one])
                mat1 =( A1 * model[one]) 
                mat2 =( A2 * model[one]) 
            else:
                try:
                    if firs < linh:
                        mat1 = mat1 + ( A1 * model[one]) 
                        mat2 = mat2 + ( A1 * model[one]) 
                    else:
                        y.append(int(one))
                except:
                    print(one+" linha: "+str(num))
            firs = firs+1
            #print(one)
            #print(model[one])
        #print('total')
        X1.append(mat1)
        X2.append(mat2)
    arq1.write(str(X1)+"\n")
    arq2.write(str(X2)+"\n")
    arqy  = None
    arqy  = open("y.txt",'w')
    arqy.write(str(y))
    arqy.close()
    arqy  = None
    arq1.close()
    arq1  = None
    arq2.close()
    arq2  = None

def somaProbpSw(txt,nmdt,sw): #txt: nome_do_corpus ; nmdt: arquivo_das_respostas ; sw: nome_arquivo_stopwords
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
    numlin = len(model.wv.vocab)
#    print(numlin)
    
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
    
    arq1  = codecs.open(nmvc+"-2-peso1-st.txt",'w','ascii')
    arq2  = codecs.open(nmvc+"-2-peso2-st.txt",'w','ascii')
    num   = 0
    X1    = []
    X2    = []
    y     = []

    linha = 0
    pala  = ''
    arqc  = codecs.open("counter.txt",'r','utf-8')
    liine  = arqc.read()
    liine  = liine.replace(" ","")
    liine  = liine.replace("':",',')
    liine  = liine.replace("u'","")
    cnt   = {}
    for word in liine.split(','):
        count = word
        if linha == 1:
            cnt[pala] = count
            linha = 0
        else:
            pala = word
            linha = 1
    arqc.close()
    arqc  = None
    
    for line in sp:
        #print('Resposta '+str(num+1))
        num  = num + 1
        mat1  = None
        mat2  = None
        firs = 1
        fora = 0
        linh = len(line.split())
        a1   = np.float32(0.001)
        a2   = np.float32(0.0001)
        for one in line.split():
            if one not in stw:
                prob = np.int32(cnt[one])/numlin
                A1   = a1/(a1 + prob)
                A2   = a2/(a2 + prob)
                try:
                    if firs == 1:
#                        print(np.int32(cnt[one]))
                        mat1 =( A1 * model[one])
                        mat2 =( A2 * model[one])
                    else:
                        if firs + fora < linh:
                            mat1 = mat1 + ( A1 * model[one]) 
                            mat2 = mat2 + ( A1 * model[one]) 
                        else:
                            y.append(int(one))
                    firs = firs+1
                except:
                    print(one+" linha: "+str(num))
            else:
                fora += 1
#                print("..."+one+"... stw: "+str(num))
            #firs = firs+1
            #print(one)
            #print(model[one])
        #print('total')
        X1.append(mat1)
        X2.append(mat2)
    arq1.write(str(X1)+"\n")
    arq2.write(str(X2)+"\n")
    arqy  = None
    arqy  = open("y.txt",'w')
    arqy.write(str(y))
    arqy.close()
    arqy  = None
    arq1.close()
    arq1  = None
    arq2.close()
    arq2  = None
    
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
    somaProbp(i,dados)
    somaProbpSw(i,dados,sw)
