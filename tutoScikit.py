#encoding: utf-8
import sys,logging
from pprint import pprint
from sklearn.svm import SVC
import numpy as np
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MultiLabelBinarizer
from decimal import *
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

nm=str(sys.argv[1])
arq=open(nm,'r')
line=arq.read()
x=line.split('\n')
p=[]
X=[]
x2=[]
y=[1,0,2,2,1,1,0,0,1,1,1,0,1,1,1,1,2,0,1,1,1,1,1,1,0,1,2,1,2,1,0,0,2,0,0,0,0,0,1,1]#40
#for num in range(0,33):
a=[1,0,2,2,1,1,0,0,1,1,1,0,1,1,1,1,2,0,1,1,1,1,1,1,0,1,2,1,2,1,0,0,2,0,0,0,0,0,1,1,1,0,0,1,0,0,0,0,1,0,0,1,0,1,1,0,0,1,1,1,1,1]#62
for num in range(0,62):
    if num < 40:
        p=map(float, x[num].split())
        X.append(p)
    else:
        p=map(float, x[num].split())
        x2.append(p)
    
#X=np.asarray(X).dtype
#y=np.asarray(y).dtype
#print(X)
#print(y)
#y=np.dtype(np.int64)
classif = OneVsRestClassifier(estimator=SVC(random_state=0))
Y = LabelBinarizer().fit_transform(y)
classif.decision_function_shape= 'ovr'
pp=classif.fit(X, Y).predict(X)
p1=classif.fit(X, y).predict(X)
pprint(pp)
print("Train:"+str(y))
print(str(p1))
p2=classif.predict(x2)
print("Predict:  "+str(a[len(y):]))
print("x2 "+str([p2]))