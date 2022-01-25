#encoding: utf-8
"""
Tutorial para execucao de k-fold cross-validation e grid-search.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import sys
import time

from utilitarios import gera_pickle
from utilitarios import carrega_pickle
from utilitarios import report

from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

from sklearn.decomposition import IncrementalPCA
from sklearn.random_projection import GaussianRandomProjection
from sklearn.random_projection import SparseRandomProjection


def kfold_resultados(data_file,nome):
    #data_file = str(sys.argv[1])# 1º argumento nome do arquivo dos vetores de todas as respostas ex: 'soma_mc5s100w7.w2v.txt'.
    #nome = str(sys.argv[2])# segundo argumento nome para o pickle, estou utilizando o mesmo nome do corpus para padronizar.

    # essa parte do código vai gerar um arquivo 'pickle' serializado contendo os
    # dados das respostas (vetores) e a pontuação de cada uma - só precisar ser
    # executado na primeira vez, depois pode deixar comentado (inclusive o import)
    targets = [1, 0, 2, 2, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 2, 0, 1, 1, 1, 1, 1,
               1, 0, 1, 2, 1, 2, 1, 0, 0, 2, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0,
               0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1]
    gera_pickle(data_file, targets, nome+".pkl")


    X, y = carrega_pickle(nome+".pkl")

    # aqui definimos a forma das divisões para o K-fold - quanto maior o número
    # de folds, mais demorada (número de folds = repetições)
    folds = 10  # precisa ser maior que 2 - eu recomendo pelo menos 10
    kfold = KFold(n_splits=folds,  # número de divisões (folds)
                  shuffle=True)

    # definição do algoritmo - se quiser definir mais do que 1 para aproveitar a
    # execução do script, terás que criar o objeto do algoritmo e colocá-lo na lista
    # de classifiers, definir os parâmetros de busca (ver abaixo) e chamar os
    # métodos no final do arquivo
    svm = SVC()
    svm2 = SGDClassifier()
    svm3 = GaussianNB()
    svm4 = KNeighborsClassifier()
    svm5 = RandomForestClassifier()
    classifiers = [svm,svm2,svm3,svm4,svm5]

    # aqui definimos os parâmetros para que a busca teste no algoritmo e nos diga
    # qual o melhor - conforme se muda o algoritmo, esses parâmetros mudam também
    # recomendo sempre uma leitura da documentação de cada algoritmo na página do
    # sickit-learn para verificar os parâmetros disponíveis e quais fazem sentido
    # para testar - quanto mais parâmetros incluir aqui, mais demorada a busca
    # sempre em formato de ``python dictionary''
    svm_param_grid = {
        'kernel': ('linear', 'rbf', 'sigmoid', 'poly'),
        'C': [1, 10, 100, 1000],
        'gamma': ['auto', 1e-2, 1e-3, 1e-4, 1e-5],
        'degree': [2, 3],
        'coef0': [0.0, 0.1, 0.01]
    }
    svm2_param_grid = {
        'loss': ('hinge','log','squared_hinge','perceptron'),
        'penalty': ('none','l1','l2','elasticnet'),
        'alpha': [0.1 , 0.01 , 0.001 , 0.0001],
        'learning_rate': ('constant','optimal'),
        'eta0': [0.1 , 0.01, 0.001]
    }
    svm3_param_grid = {
        'priors': [None]
    }
    svm4_param_grid = {
        'n_neighbors': [3, 5, 10],
        'weights': ('uniform','distance'),
        'algorithm': ('ball_tree', 'kd_tree', 'brute'),
        'leaf_size': [10, 30, 5, 15, 20]
    }
    svm5_param_grid = {
        'n_estimators': [2, 3, 5, 7, 10],
        'criterion': ('gini','entropy'),
        'max_features': ['auto', 2, 1,None],
    }


    grids = [svm_param_grid,svm2_param_grid,svm3_param_grid,svm4_param_grid,svm5_param_grid]

    # gera uma lista de tuplas entre classifiers e grids para que cada um fique na
    # posição correta
    grid_params = zip(classifiers, grids)

    arq1 = open('Result-SomaRed-pca_n_' + data_file , 'w' )
    arq2 = open('Result-SomaRed-pca_w_' + data_file , 'w' )
    arq3 = open('Result-SomaRed-gaussi_'+ data_file , 'w' )
    arq4 = open('Result-SomaRed-sparse_'+ data_file , 'w' )

    pca_regular = IncrementalPCA(n_components=1, whiten=False)
    pca_whiten = IncrementalPCA(n_components=1, whiten=True)
    # para as projeções vale a mesma coisa do primeiro componente
    gaussian_projection = GaussianRandomProjection(n_components=1)
    sparse_projection = SparseRandomProjection(n_components=1)
    respostas_pca_regular = []
    respostas_pca_whiten = []
    respostas_gaussian_projection = []
    respostas_sparse_projection = []

    for matriz in X:
        #print(XX)
        # aqui temos que aplicar para cada resposta os métodos pois cada matriz
        # será diferente e os métodos são baseados na própria matriz. não teria
        # sentido aplicar a mesma coisa para todas elas
    #print(matriz)
    # primeiro PCA sem whitening
        component = pca_regular.fit_transform(matriz,y)
        component = component.reshape([-1])
        respostas_pca_regular.append(component)
        # depois PCA com whitening
        component = pca_whiten.fit_transform(matriz,y)
        component = component.reshape([-1])
        respostas_pca_whiten.append(component)

        # gaussian projection
        component = gaussian_projection.fit_transform(matriz,y)
        component = component.reshape([-1])
        respostas_gaussian_projection.append(component)

        # sparse projection
        component = sparse_projection.fit_transform(matriz,y)
        component = component.reshape([-1])
        respostas_sparse_projection.append(component)

    #print(respostas_pca_regular             ,file=arq1)
    #print(respostas_pca_whiten              ,file=arq2)
    #print(respostas_gaussian_projection     ,file=arq3)
    #print(respostas_sparse_projection       ,file=arq4)


    # aqui fazemos a busca - neste caso a busca é por força bruta, ou seja, vai
    # testar todas as combinações que incluirmos no dicionário de parâmetros - há
    # também a opção de se buscar randomicamente, mas precisariamos definir
    # distribuições ao invés de parâmetros, mas os resultados são bastante parecidos
    # a busca vai ser feita pelo ``score'' que definirmos - no artigo anterior foi
    # utilizado a percentagem de acertos (se não me engano). Dependendo da
    # comparação resultados podemos utilizar outras métricas já que temos os dados
    # da classificação anterior, mas por hora deixamos igual

    for _, (classifier, params) in enumerate(grid_params):

        print("Buscando para algoritmo: {0}\n".format(classifier.__class__),file=arq1)
        print("Buscando para algoritmo: {0}\n".format(classifier.__class__),file=arq2)
        print("Buscando para algoritmo: {0}\n".format(classifier.__class__),file=arq3)
        print("Buscando para algoritmo: {0}\n".format(classifier.__class__),file=arq4)

        grid_search1 = GridSearchCV(estimator=classifier,  # algoritmo que será testado
                                   param_grid=params,  # parâmetros de busca
                                   cv=kfold,  # objeto que vai gerar as divisões
                                   scoring='accuracy')  # score que será utilizado

        grid_search2 = GridSearchCV(estimator=classifier,  # algoritmo que será testado
                                   param_grid=params,  # parâmetros de busca
                                   cv=kfold,  # objeto que vai gerar as divisões
                                   scoring='accuracy')  # score que será utilizado

        grid_search3 = GridSearchCV(estimator=classifier,  # algoritmo que será testado
                                   param_grid=params,  # parâmetros de busca
                                   cv=kfold,  # objeto que vai gerar as divisões
                                   scoring='accuracy')  # score que será utilizado

        grid_search4 = GridSearchCV(estimator=classifier,  # algoritmo que será testado
                                   param_grid=params,  # parâmetros de busca
                                   cv=kfold,  # objeto que vai gerar as divisões
                                   scoring='accuracy')  # score que será utilizado

        # aqui nós imprimimos o resultado - o método report vai imprimir as ``top''
        # melhores combinações encontrada na busca - o que interessa é a primeira,
        # as outras são apenas para satisfazer curiosidade - os parâmetros impressos
        # são aqueles que teríamos que usar para gerar o classificador se fosse
        # utilizarmos em outro lugar
        #top = 5 essa variavel não tem motivos de utilizar ja que o numero colocado no n_top é até qual combinação vai mostrar e não as 'top' melhores! 




        start = time.time()
        grid_search1.fit(respostas_pca_regular, y)
        combinacoes1 = len(grid_search1.cv_results_["rank_test_score"])
        print("Tempo de busca: {:.2f} secs para {:d} candidatos.".format(
              (time.time() - start), combinacoes1),file=arq1)
        report(grid_search1.cv_results_, n_top=combinacoes1,arq=arq1)
        
        grid_search2.fit(respostas_pca_whiten, y)
        combinacoes2 = len(grid_search2.cv_results_["rank_test_score"])
        print("Tempo de busca: {:.2f} secs para {:d} candidatos.".format(
              (time.time() - start), combinacoes2),file=arq2)
        report(grid_search2.cv_results_, n_top=combinacoes2,arq=arq2)
        
        grid_search3.fit(respostas_gaussian_projection, y)
        combinacoes3 = len(grid_search3.cv_results_["rank_test_score"])
        print("Tempo de busca: {:.2f} secs para {:d} candidatos.".format(
              (time.time() - start), combinacoes3),file=arq3)
        report(grid_search3.cv_results_, n_top=combinacoes3,arq=arq3)
        
        grid_search4.fit(respostas_sparse_projection, y)
        combinacoes4 = len(grid_search4.cv_results_["rank_test_score"])
        print("Tempo de busca: {:.2f} secs para {:d} candidatos.".format(
              (time.time() - start), combinacoes4),file=arq4)
        report(grid_search4.cv_results_, n_top=combinacoes4,arq=arq4)

    arq1.close()
    arq1=None
    arq2.close()
    arq2=None
    arq3.close()
    arq3=None
    arq4.close()
    arq4=None        
    #arq.close()
    #arq=None

ar=None
ar=open(str(sys.argv[1]))#corpusfile
#nome=str(sys.argv[2])
tex=ar.read()
ar.close()
ar=None
arqs=tex.split('\n')
for i in arqs:
    print('soma_'+i+"-vec.txt")
    l='soma_'+i+"-vec.txt"
    kfold_resultados(data_file=l,nome=i)
    print('soma_'+i+"-vec-st.txt")
    l='soma_'+i+"-vec-st.txt"
    kfold_resultados(data_file=l,nome=i)
