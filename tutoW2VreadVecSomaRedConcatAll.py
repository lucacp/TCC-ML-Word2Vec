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

from sklearn.decomposition import IncrementalPCA
from sklearn.random_projection import GaussianRandomProjection
from sklearn.random_projection import SparseRandomProjection


def concatena(nmvc,nmdt):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    #nmvc  = str(sys.argv[1]) #nome_corpus
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
    #arq   = codecs.open(nmvc+"-conc.txt",'w','ascii')
    num   = 0
    X     = []
    XX    = []
    y     = []
    for line in sp:
        #print('#',file=arq)
        num  = num+1
        firs = 1
        linh = len(line.split())
        for one in line.split():
            if firs == 1:
                vetor  = model[one]
                shape0 = vetor.shape[0]
                mat    = vetor.reshape(shape0, 1)
                X.append(mat)
            else:
                if firs < linh:
                    try:
                        vetor  = model[one]
                        shape0 = vetor.shape[0]
                        mat   += vetor.reshape(shape0, 1)
                        X.append(mat)
                    except:
                        print(one+" linha: "+str(num))
                else:
                    y.append(int(one))
            firs = firs+1
            #print(one)
            #print(model[one])
        #print('total')
        Y = np.concatenate( X, axis=1)
        XX.append(Y)
        #X.append(mat)
    arq1  = open('SomaConcat-pca_n_' + nmvc + ".txt" , 'w' )
    arq2  = open('SomaConcat-pca_w_' + nmvc + ".txt" , 'w' )
    arq3  = open('SomaConcat-gaussi_'+ nmvc + ".txt" , 'w' )
    arq4  = open('SomaConcat-sparse_'+ nmvc + ".txt" , 'w' )

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
    print(respostas_pca_regular ,file=arq1)
    print(respostas_pca_whiten ,file=arq2)
    print(respostas_gaussian_projection,file=arq3)
    print(respostas_sparse_projection ,file=arq4)

    arq1.close()
    arq1  = None
    arq2.close()
    arq2  = None
    arq3.close()
    arq3  = None
    arq4.close()
    arq4  = None        
    #arq.close()
    #arq   = None


def concatenaSw(nmvc,nmdt,sw):
    #nmvc  = str(sys.argv[1]) #nome_corpus
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
    #nmdt  = str(sys.argv[2]) #arquivo_das_respostas
    arq   = codecs.open(nmdt,'r','utf-8')
    line  = arq.read()
    line  = tokenize(line)
    sp    = line.split('\n')
    arq.close()
    arq   = None
    
    arq   = codecs.open(sw,'r','utf-8')
    stp   = arq.read()
    arq.close()
    stp   = tokenize(stp)
    stw   = set(stp.split())
    arq   = None
    
    #arq   = codecs.open(nmvc+"-conc-st.txt",'w','ascii')
    num   = 0
    X     = []
    XX    = []
    y     = []
    for line in sp:
        #print('#',file=arq)
        num  = num+1
        firs = 1
        mat  = None
        linh = len(line.split())
        for one in line.split():
            if one not in stw:
                if firs == 1:
                    mat    = vetor  = model.wv[one]
                    shape0 = vetor.shape[0]
                    X.append(vetor.reshape(shape0, 1))
                    #X.append(mat)
                else:
                    if firs < linh:
                        try:
                            vetor  = model.wv[one]
                            shape0 = vetor.shape[0]
                            mat    = vetor + mat
                            X.append(mat.reshape(shape[0],1))
                        except:
                            print(one+" linha: "+str(num))
                    else:
                        y.append(int(one))
                firs = firs+1
            #print(one)
            #print(model[one])
        #print('total')
        Y = np.concatenate( X, axis=1)
        XX.append(Y)
        #X.append(mat)
    arq1  = open('SomaConcat-pca_n_' + nmvc + "-st.txt" , 'w' )
    arq2  = open('SomaConcat-pca_w_' + nmvc + "-st.txt" , 'w' )
    arq3  = open('SomaConcat-gaussi_'+ nmvc + "-st.txt" , 'w' )
    arq4  = open('SomaConcat-sparse_'+ nmvc + "-st.txt" , 'w' )

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
    print(respostas_pca_regular          ,file=arq1)
    print(respostas_pca_whiten           ,file=arq2)
    print(respostas_gaussian_projection  ,file=arq3)
    print(respostas_sparse_projection    ,file=arq4)

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
    concatena(i,dados)
    concatenaSw(i,dados,sw)
