#encoding: utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys, codecs
import gensim, logging
from gensim.models import Word2Vec
from pprint import pprint
#from sklearn.svm import SVC
import numpy as np
#from sklearn.multiclass import OneVsRestClassifier
#from sklearn.preprocessing import LabelBinarizer
#from sklearn.preprocessing import MultiLabelBinarizer
from tokenizacao import tokenize


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
nmvc  = str(sys.argv[1]) #nome_corpus
model = Word2Vec.load(nmvc)
model.init_sims(replace=True)
#pprint(model.wv.vocab)
arq   = None
try:
    arq = codecs.open("treinamento"+nmvc+".txt",'r','utf-8')
except FileNotFoundError:
    arq = codecs.open("treinamento"+nmvc+".txt",'w','utf-8')
    pprint(model.wv.vocab,arq)
arq.close()
arq   = None
nmdt  = str(sys.argv[2]) #arquivo_das_respostas
arq   = codecs.open(nmdt,'r','utf-8')
line  = arq.read()
line  = tokenize(line)
sp    = line.split('\n')
arq.close()
arq   = None
arq   = codecs.open(nmvc+"-conc.txt",'w','ascii')
num   = 0
#X    = []
y     = []
for line in sp:
    print('#',file=arq)
    num  = num+1
    firs = 1
    linh = len(line.split())
    for one in line.split():
        if firs == 1:
            print(str(model[one]),file=arq)
        else:
            if firs < linh:
                try:
                    print(str(model[one]),file=arq)
                except:
                    print(one+" linha: "+str(num))
            else:
                y.append(int(one))
        firs = firs+1
        #print(one)
        #print(model[one])
    #print('total')
    #X.append(mat)
#arq.write(str(y))
arq.close()
arq   = None
#print(X)
#print(y)
#classif = OneVsRestClassifier(estimator=SVC(random_state=0))
#Y = LabelBinarizer().fit_transform(y)
#classif.fit(X, Y).predict(X)