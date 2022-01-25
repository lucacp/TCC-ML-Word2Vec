#encoding: utf-8
import sys, codecs
import gensim, logging
from gensim.models import Word2Vec
from pprint import pprint
from sklearn.svm import SVC
import numpy as np
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MultiLabelBinarizer
from tokenizacao import tokenize

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
nome = str(sys.argv[2])
model = Word2Vec.load(nome)
model.init_sims(replace=True)
#pprint(model.wv.vocab)
nm=str(sys.argv[1])
arq=codecs.open(nm,'r','utf-8')
line=arq.read()
line=tokenize(line)
sp=line.split('\n')
num = 0
X=[]
y=[]
for line in sp:
    print('Resposta '+str(num+1))
    num=num+1
    mat=None
    firs=1
    linh=len(line.split())
    for one in line.split():
        try:
            if firs == 1:
                mat=model[one]
            else:
                print(one)
                print(model[one])
                if firs < linh:
                    mat=mat+model[one]
                else:
                    y.append(int(one))
        except:
            print(one+" linha: "+str(num))
        firs=firs+1
    print('total')
    X.append(mat)
    print(mat)
#print(X)
#print(y)
#classif = OneVsRestClassifier(estimator=SVC(random_state=0))
#Y = LabelBinarizer().fit_transform(y)
#classif.fit(X, Y).predict(X)