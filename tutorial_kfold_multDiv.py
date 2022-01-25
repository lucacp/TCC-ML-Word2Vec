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
                                   scoring='accuracy')  # score que será utilizado

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
    arq=None

ar=None
ar=open(str(sys.argv[1]))#corpusfile
#nome=str(sys.argv[2])
tex=ar.read()
ar.close()
ar=None
arqs=tex.split('\n')
for i in arqs:
    print('mult_'+i+"-multdiv.txt")
    l='mult_'+i+"-multdiv.txt"
    kfold_resultados(data_file=l,nome=i)
    print('mult_'+i+"-multdiv-st.txt")
    l='mult_'+i+"-multdiv-st.txt"
    kfold_resultados(data_file=l,nome=i)
