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

from tokenizacao import tokenize
from sklearn.decomposition import IncrementalPCA
from sklearn.random_projection import GaussianRandomProjection
from sklearn.random_projection import SparseRandomProjection


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
nmvc  = str(sys.argv[1]) #nome_corpus
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
nmdt  = str(sys.argv[2]) #arquivo_respostas
arq   = codecs.open(nmdt,'r','utf-8')
line  = arq.read()
line  = tokenize(line)
sp    = line.split('\n')
arq.close()
arq   = None
#arq   = codecs.open(nmvc+"-vec.txt",'w','ascii')
num   = 0
XX    = []
X     = []
y     = []
for line in sp:
    #print('Resposta '+str(num+1))
    num  = num + 1
    mat  = None
    met  = None
    firs = 1
    linh = len( line.split() )
    for one in line.split():
        if firs == 1:
            mat    = vetor  = model[one]
            shape0 = vetor.shape[0]
            met    = vetor.reshape(shape0, 1)
            #print(mat.shape,type(mat))
        else:
            if firs < linh:
                try:
                    vetor  = model[one]
                    shape0 = vetor.shape[0]
                    mat   += vetor 
                    met    = mat.reshape(shape0, 1)
                except:
                    print(one+" linha: "+str(num))
            else:
                y.append(int(one))
            
        firs = firs+1
        #print(one)
        #print(model[one])
    #print('total')
    #print(mat)
    #print(mat.shape[0],type(mat),y.shape,type(y))
    if met != None:
        X.append(met)
    #XX.append(y[len(y)-1])
    #X.append(mat)
#print(X.shape,type(X),y.shape,type(y))
#for i in X:
#    print(i.shape)
    Y     = np.concatenate( X, axis=1)
    XX.append(Y)
#arq.write(str(X)+"\n")
#arq.write(str(y))
#arq.close()
#arq   = None
#print(X)
#print(y)

arq1 = open('SomaRed-pca_n_' + nmvc + ".txt" , 'w' )
arq2 = open('SomaRed-pca_w_' + nmvc + ".txt" , 'w' )
arq3 = open('SomaRed-gaussi_'+ nmvc + ".txt" , 'w' )
arq4 = open('SomaRed-sparse_'+ nmvc + ".txt" , 'w' )

pca_regular = IncrementalPCA(n_components=1, whiten=False)
pca_whiten = IncrementalPCA(n_components=1, whiten=True)
# para as projeções vale a mesma coisa do primeiro componente
gaussian_projection = GaussianRandomProjection(n_components=1)
sparse_projection = SparseRandomProjection(n_components=1)
respostas_pca_regular = []
respostas_pca_whiten = []
respostas_gaussian_projection = []
respostas_sparse_projection = []

for matriz in XX:
    #print(XX)
    # aqui temos que aplicar para cada resposta os métodos pois cada matriz
    # será diferente e os métodos são baseados na própria matriz. não teria
    # sentido aplicar a mesma coisa para todas elas
#print(matriz)
# primeiro PCA sem whitening
    component = pca_regular.fit_transform(matriz)
    component = component.reshape([-1])
    respostas_pca_regular.append(component)

    # depois PCA com whitening
    component = pca_whiten.fit_transform(matriz)
    component = component.reshape([-1])
    respostas_pca_whiten.append(component)

    # gaussian projection
    component = gaussian_projection.fit_transform(matriz)
    component = component.reshape([-1])
    respostas_gaussian_projection.append(component)

    # sparse projection
    component = sparse_projection.fit_transform(matriz)
    component = component.reshape([-1])
    respostas_sparse_projection.append(component)

print(respostas_pca_regular             ,file=arq1)
print(respostas_pca_whiten              ,file=arq2)
print(respostas_gaussian_projection     ,file=arq3)
print(respostas_sparse_projection       ,file=arq4)

arq1.close()
arq1=None
arq2.close()
arq2=None
arq3.close()
arq3=None
arq4.close()
arq4=None        
#arq.close()
#arq   = None
