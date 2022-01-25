#encoding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from utilitarios import gera_pickle
from utilitarios import carrega_pickle
from utilitarios import report
import sys, codecs
import time
import gensim
from gensim.models import Word2Vec
from pprint import pprint
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV, KFold
import numpy as np
from tokenizacao import tokenize

def resultadoFinal(novos,dest):
    f    = open('sklearn_parametros_'+dest,'r')
    r    = f.read()
    r    = r.replace("'",",")
    r    = r.replace("(",",")
    r    = r.replace(")",",")
    r    = r.replace("[","")
    r    = r.replace("]","")
    r    = r.replace(" ","")
    r    = r.replace(",,",",")
    arq1 = open(dest,'w')
    arq2 = open(novos,'r')
    res  = arq2.read().split('\n')
    arq2.close()
    arq2 = None
    flag = 0
    num  = 0
    cont = 0
    for line in r.split('\n'):
        if flag > 0:
            cont -= 1
        flag = 0
        num  = 0
        cont+= 1
        for word in line.split(','):
            if flag > 0:
                continue
            if word == 'SGDClassifier':
                flag = 1
                continue
            if word != '':
                res[num] +='; '+str(cont)+': '+str(word)
            else:
                num -=1
            num += 1
    for line in res:
        print(line,file=arq1)
    arq1.close()
    arq1 = None
#
def kfold_resultados(data_file,nome,file2,dest):
    #data_file = str(sys.argv[1])# 1º argumento nome do arquivo dos vetores de todas as respostas ex: 'soma_mc5s100w7.w2v.txt'.
    #nome = str(sys.argv[2])# segundo argumento nome para o pickle, estou utilizando o mesmo nome do corpus para padronizar.

    # essa parte do código vai gerar um arquivo 'pickle' serializado contendo os
    # dados das respostas (vetores) e a pontuação de cada uma - só precisar ser
    # executado na primeira vez, depois pode deixar comentado (inclusive o import)
    f = open('y.txt','r')
    r = f.read()
    r = r.replace('[','')
    r = r.replace(']','')
    r = r.replace(',','')
    targets = r.split()
    #print(targets)
    f.close()
    f = None
              #[1, 0, 2, 2, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 2, 0, 1, 1, 1, 1, 1,
              # 1, 0, 1, 2, 1, 2, 1, 0, 0, 2, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0,
              # 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1]
    gera_pickle(data_file, targets, nome+".pkl")
    targets = None
    targets = []
    f = open(file2,'r')
    r = f.read().split('\n')
    d = len(r)
    #print(r)
    f.close()
    for i in range(d-1):
        targets.append(0)
    #print(targets)
    f = None
    d = None
    gera_pickle(file2, targets, nome+"_2.pkl")
    
    X , y  = carrega_pickle(nome+".pkl")
    X2, y2 = carrega_pickle(nome+"_2.pkl")
    
    # aqui definimos a forma das divisões para o K-fold - quanto maior o número
    # de folds, mais demorada (número de folds = repetições)
    folds = 10  # precisa ser maior que 2 - eu recomendo pelo menos 10
    kfold = KFold(n_splits=folds,  # número de divisões (folds)
                  shuffle=True)

    # definição do algoritmo - se quiser definir mais do que 1 para aproveitar a
    # execução do script, terás que criar o objeto do algoritmo e colocá-lo na lista
    # de classifiers, definir os parâmetros de busca (ver abaixo) e chamar os
    # métodos no final do arquivo
    svm = SGDClassifier()
    classifiers = [svm]

    # aqui definimos os parâmetros para que a busca teste no algoritmo e nos diga
    # qual o melhor - conforme se muda o algoritmo, esses parâmetros mudam também
    # recomendo sempre uma leitura da documentação de cada algoritmo na página do
    # sickit-learn para verificar os parâmetros disponíveis e quais fazem sentido
    # para testar - quanto mais parâmetros incluir aqui, mais demorada a busca
    # sempre em formato de ``python dictionary''
    svm_param_grid = {
        'loss': ('hinge','log','squared_hinge','perceptron'),
        'penalty': ('none','l1','l2','elasticnet'),
        'alpha': [0.1 , 0.01 , 0.001 , 0.0001],
        'learning_rate': ('constant','optimal'),
        'eta0': [0.1 , 0.01, 0.001]
    }
    #print(str(X2))
    arq2 = open('sklearn_parametros_'+dest,'w')
    svm1 = SGDClassifier(loss='',penalty=1000,alpha=1e-2,learning_rate=2,eta0=0.0)
    svm2 = SGDClassifier(loss='',penalty=1000,alpha=1e-2,learning_rate=2,eta0=0.1)
    svm3 = SGDClassifier(loss='',penalty=1000,alpha=1e-2,learning_rate=2,eta0=0.01)
    svm4 = SGDClassifier(loss='',penalty=1000,alpha=1e-2,learning_rate=3,eta0=0.0)
    svm5 = SGDClassifier(loss='',penalty=1000,alpha=1e-2,learning_rate=3,eta0=0.1)
    svm6 = SGDClassifier(loss='',penalty=1000,alpha=1e-2,learning_rate=3,eta0=0.01)
    p1 = svm1.fit(X, y)
    p2 = svm2.fit(X, y)
    p3 = svm3.fit(X, y)
    p4 = svm4.fit(X, y)
    p5 = svm5.fit(X, y)
    p6 = svm6.fit(X, y)
    print('SGDClassifier(kernel=sigmoid,C=1000,gamma=1e-2,degree=2,coef0=0.0)',file=arq2)
    print(p1.predict(X2),file=arq2)
    print('SGDClassifier(kernel=sigmoid,C=1000,gamma=1e-2,degree=2,coef0=0.1)',file=arq2)
    print(p2.predict(X2),file=arq2)
    print('SGDClassifier(kernel=sigmoid,C=1000,gamma=1e-2,degree=2,coef0=0.01)',file=arq2)
    print(p3.predict(X2),file=arq2)
    print('SGDClassifier(kernel=sigmoid,C=1000,gamma=1e-2,degree=3,coef0=0.0)',file=arq2)
    print(p4.predict(X2),file=arq2)
    print('SGDClassifier(kernel=sigmoid,C=1000,gamma=1e-2,degree=3,coef0=0.1)',file=arq2)
    print(p5.predict(X2),file=arq2)
    print('SGDClassifier(kernel=sigmoid,C=1000,gamma=1e-2,degree=3,coef0=0.01)',file=arq2)
    print(p6.predict(X2),file=arq2)
    #print(p1.score(X,y))
    #print(p2.score(X,y))
    #print(p3.score(X,y))
    #print(p4.score(X,y))
    #print(p5.score(X,y))
    #print(p6.score(X,y))

    grids = [svm_param_grid]

    # gera uma lista de tuplas entre classifiers e grids para que cada um fique na
    # posição correta
    grid_params = zip(classifiers, grids)

    arq = open('Result_'+data_file,'w')

    # aqui fazemos a busca - neste caso a busca é por força bruta, ou seja, vai
    # testar todas as combinações que incluirmos no dicionário de parâmetros - há
    # também a opção de se buscar randomicamente, mas precisariamos definir
    # distribuições ao invés de parâmetros, mas os resultados são bastante parecidos
    # a busca vai ser feita pelo ``score'' que definirmos - no artigo anterior foi
    # utilizado a percentagem de acertos (se não me engano). Dependendo da
    # comparação resultados podemos utilizar outras métricas já que temos os dados
    # da classificação anterior, mas por hora deixamos igual
    for _, (classifier, params) in enumerate(grid_params):

        print("Buscando para algoritmo: {0}\n".format(classifier.__class__),file=arq)

        grid_search = GridSearchCV(estimator=classifier,  # algoritmo que será testado
                                   param_grid=params,  # parâmetros de busca
                                   cv=kfold,  # objeto que vai gerar as divisões
                                   scoring='accuracy', # score que será utilizado
                                   refit=True)  

        start = time.time()
        grid_search.fit(X, y)
        # aqui nós imprimimos o resultado - o método report vai imprimir as ``top''
        # melhores combinações encontrada na busca - o que interessa é a primeira,
        # as outras são apenas para satisfazer curiosidade - os parâmetros impressos
        # são aqueles que teríamos que usar para gerar o classificador se fosse
        # utilizarmos em outro lugar
        #top = 5 essa variavel não tem motivos de utilizar ja que o numero colocado no n_top é até qual combinação vai mostrar e não as 'top' melhores! 
        combinacoes = len(grid_search.cv_results_["rank_test_score"])
        print("Tempo de busca: {:.2f} secs para {:d} candidatos.".format(
              (time.time() - start), combinacoes),file=arq)
        report(grid_search.cv_results_, n_top=combinacoes,arq=arq)
    arq.close()
    arq  = None
    arq2.close()
    arq2 = None

def transfSomaProb(nm):
#    nm   = str(sys.argv[1])
    arq  = open(nm,'r')
    line = arq.read()
    line = line.replace('array','array,')
    line = line.replace('[','')
    line = line.replace(']','')
    line = line.replace('(','')
    line = line.replace(')','')
    #line = line.replace('=','')
    line = line.replace(' ','')
    line = line.replace('\n',',')
    vec  = ''
    #y    = ''
    num  = 0
    arq.close()
    arq  = None
    ar   = open('soma_'+nm,'w')
    #print(line)
    for x in line.split(','):
    #    print(x)
        if x == 'None':
            num = 0
            vec=vec+'\n'
            ar.write(vec)
        else:
            if x == 'array':
                if num > 0:
                    vec = vec + '\n'
                    ar.write(vec)
                num += 1 
                vec  = None
                vec  = ''
            else:
                #if num != 0:
                    #vec=vec+str(x)+' '
                #else:
                    #y=y+str(x)+' '
                vec = vec + str(x) + ' '
    #print(vec)
    #print(y)
    if num > 0:
        ar.write(vec)#+y)
    ar.close()
    ar = None


def somaProbSw(txt,nmdt,sw,nmdt2): #txt: nome_do_corpus ; nmdt: arquivo_das_respostas ; sw: nome_arquivo_stopwords
    nmvc  = txt
    model = Word2Vec.load(nmvc)
    model.init_sims(replace=True)
    arq   = None
    numlin = len(model.wv.vocab)
#    numlin *= 1.1
    arq   = codecs.open(sw,'r','utf-8')
    stp   = arq.read()
    arq.close()
    stp   = tokenize(stp)
    stw   = set(stp.split())
    arq   = None
    
    arq   = codecs.open(nmdt,'r','utf-8')
    line  = arq.read()
    line  = tokenize(line)
    sp    = line.split('\n')
    arq.close()
    arq   = None
    
    arq   = codecs.open(nmdt2,'r','utf-8')
    line2  = arq.read()
    line2  = tokenize(line2)
    sp2    = line2.split('\n')
    arq.close()
    arq   = None
    
    arq   = codecs.open(nmvc+"-prob-st.txt",'w','ascii')
    num   = 0
    X     = []
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
        mat  = None
        firs = 1
        fora = 0
        linh = len(line.split())
        for one in line.split():
            if one not in stw:
                try:
                    if firs == 1:
#                        print(np.int32(cnt[one]))
                        mat = (model[one] * np.int32(cnt[one]))/numlin
                    else:
                        if firs + fora < linh:
                            mat = mat + (model[one] * np.int32(cnt[one]))/numlin
                        if firs + fora == linh:
                            y.append(int(one))
                    firs = firs+1
            
                except:
                    print(one+" linha: "+str(num))
            else:
                fora = fora + 1
#                print("..."+one+"... stw: "+str(num))
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
    print( str(y) , file=arq1)
    arq1.close()
    arq1     =  None

    arq      = codecs.open(nmvc+"-2-prob-st.txt",'w','ascii')
    num      = 0
    X        = []

    for line in sp2:
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
#                        print(np.int32(cnt[one]))
                        mat = (model[one] * np.int32(cnt[one]))/numlin
                    else:
                        if firs < linh:
                            mat = mat + (model[one] * np.int32(cnt[one]))/numlin
                        if firs + fora == linh:
                            mat = mat + (model[one] * np.int32(cnt[one]))/numlin
                        #    y.append(int(one))
                    firs = firs+1
            
                except:
                    print('Palavra: "'+one+'" na linha: '+str(num)+' nao foi encontrada. Verifique se está escrita corretamente.')
            else:
                fora = fora + 1
#                print("..."+one+"... stw: "+str(num))
            #firs = firs+1
            #print(one)
            #print(model[one])
        #print('total')
        X.append(mat)
    arq.write(  str(X) + "\n")
    arq.close()
    arq      =  None
    
#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
ar    = None
#ar    = open(str(sys.argv[1]))
dados =      str(sys.argv[1])
novos =      str(sys.argv[2])
dest  =      str(sys.argv[3])
#tex   = ar.read()
#ar.close()
#ar    = None
#arqs  = tex.split('\n')
sw    = 'stopwords_pt.txt'
i     = 'mc5s200w3.w2v'
somaProbSw(i,dados,sw,novos)
transfSomaProb(i+'-prob-st.txt')
transfSomaProb(i+'-2-prob-st.txt')
kfold_resultados(data_file='soma_'+i+'-prob-st.txt',nome='X',file2='soma_'+i+'-2-prob-st.txt',dest=dest)
resultadoFinal(novos,dest)