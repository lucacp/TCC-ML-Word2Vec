#encoding: utf-8
import sys,logging
from pprint import pprint
import numpy as np
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer
#from sklearn.preprocessing import MultiLabelBinarizer
from decimal import *
from sklearn.svm import SVC
from sklearn import linear_model
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

nm=str(sys.argv[1])
arq=open(nm,'r')
line=arq.read()
x=line.split('\n')
nm2=str(sys.argv[2])
arq2=open(nm2,'r')
line2=arq2.read()
x3=line2.split('\n')
p=[]
X=[]
x2=[]
y=[1,0,2,2,1,1,0,0,1,1,1,0,1,1,1,1,2,0,1,1,1,1,1,1,0,1,2,1,2,1,0,0,2,0,0,0,0,0,1,1,1,0,0,1,0,0,0,0,1,0]#50
#for num in range(0,33):
a=[1,0,2,2,1,1,0,0,1,1,1,0,1,1,1,1,2,0,1,1,1,1,1,1,0,1,2,1,2,1,0,0,2,0,0,0,0,0,1,1,1,0,0,1,0,0,0,0,1,0,0,1,0,1,1,0,0,1,1,1,1,1]#62
for num in range(len(a)):
    if num < len(y):
        p=map(float, x[num].split())
        X.append(p)
    else:
        p=map(float, x3[num-len(y)].split())
        x2.append(p)
    
#X=np.asarray(X).dtype
#y=np.asarray(y).dtype
#print(X)
#print(y)
#y=np.dtype(np.int64)
classif = OneVsRestClassifier(estimator=SVC(kernel='sigmoid',C=1000,gamma=1e-2,degree=2,coef0=0.1))
Y       = LabelBinarizer().fit_transform(y)
classif.decision_function_shape= 'ovr'
#pp      = classif.fit(X, Y).predict(X)
p0      = classif.fit(X, y)
print("Y = "+str(y))
print("OVR_Classifier:")
#pprint(pp)
print(p0.predict(X))
p2=classif.predict(x2)
print("Predict:  "+str(a[len(y):]))
print("x2 "+str([p2]))
print(p0.score(X,y))

clf1    = None
clf1    = linear_model.SGDClassifier()
p1      = clf1.fit(X,y)
print("SGDClassifier:")
print(p1.predict(x2))
print(p1.score(X,y))

clf2    = None
clf2    = GaussianNB()
p5      = clf2.fit( X , y )
print("GaussianNB:")
print(p5.predict(x2))
print(p5.score(X,y))

clf3    = None
clf3    = KNeighborsClassifier(n_neighbors=3)
p3      = clf3.fit( X , y )
print("KNeighbors-3:")
print(p3.predict(x2))
print(p3.score(X,y))

clf4    = None
clf4    = RandomForestClassifier()
p4      = clf4.fit( X , y )
print("RandomForestClassifier:")
print(p4.predict(x2))
print(p4.score(X,y))


