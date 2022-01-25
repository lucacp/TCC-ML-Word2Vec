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

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
nmvc = str(sys.argv[1])
model = Word2Vec.load(nmvc)
model.init_sims(replace=True)
#pprint(model.wv.vocab)
arq = codecs.open("treinamento"+nmvc+".txt",'w','utf-8')
pprint(model.wv.vocab,arq)
arq.close()
arq=None
nmdt=str(sys.argv[2])
arq=codecs.open(nmdt,'r','utf-8')
line=arq.read()
line=line.replace(","," ")
line=line.replace("."," ")
line=line.replace("'"," ")
line=line.replace('"'," ")
line=line.replace(">"," ")
line=line.replace("<"," ")
line=line.replace(";"," ")
line=line.replace("="," ")
line=line.replace("!"," ")
line=line.replace("?"," ")
line=line.replace("("," ")
line=line.replace(")"," ")
line=line.replace(":"," ")
line=line.replace("["," ")
line=line.replace("]"," ")
line=line.replace(u"´"," ")
line=line.replace("#"," ")
line=line.replace(u"`"," ")
line=line.replace("{"," ")
line=line.replace("}"," ")
line=line.lower()
line=line.replace(u"á","a")
line=line.replace(u"à","a")
line=line.replace(u"ã","a")
line=line.replace(u'â',"a")
line=line.replace(u"ä","a")
line=line.replace(u"é","e")
line=line.replace(u"è","e")
line=line.replace(u"ê","e")
line=line.replace(u"ë","e")
line=line.replace(u"í","i")
line=line.replace(u"ì","i")
line=line.replace(u'î',"i")
line=line.replace(u"ï","i")
line=line.replace(u"ó","o")
line=line.replace(u"ò","o")
line=line.replace(u"õ","o")
line=line.replace(u'ô',"o")
line=line.replace(u"ö","o")
line=line.replace(u"ú","u")
line=line.replace(u"ù","u")
line=line.replace(u"û","u")
line=line.replace(u'ü',"u")
line=line.replace(u"ç","c")
sp=line.split('\n')
arq.close()
arq=None
arq = codecs.open(nmvc+"-vec.txt",'w','ascii')
num = 0
X=[]
y=[]
for line in sp:
    #print('Resposta '+str(num+1))
    num=num+1
    mat=None
    firs=1
    linh=len(line.split())
    for one in line.split():
        if firs == 1:
            mat=model[one]
        else:
            try:
                if firs < linh:
                    mat=mat+model[one]
                else:
                    y.append(int(one))
            except:
                print(one+" linha: "+str(num))
        firs=firs+1
        #print(one)
        #print(model[one])
    #print('total')
    X.append(mat)
arq.write(str(X)+"\n")
#arq.write(str(y))
arq.close()
arq=None
#print(X)
#print(y)
#classif = OneVsRestClassifier(estimator=SVC(random_state=0))
#Y = LabelBinarizer().fit_transform(y)
#classif.fit(X, Y).predict(X)