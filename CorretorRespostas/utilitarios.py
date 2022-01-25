#encoding: utf-8
"""
Tutorial para execução de k-fold cross-validation e grid-search.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pickle

import numpy as np


def gera_pickle(_arquivo, _labels, _destino):
    """ Método para gerar um arquivo pickle.

    O método carrega os vetores indicado por _arquivo e gera um ``dictionary''
    que vai ser persistido pelo módulo ``pickle''.

    Facilita na hora de carregar os dados e diminui a quantidade de código que
    precisa ser escrito.

    Args:
        _arquivo: str, caminho para o arquivo com os vetores
        _labels: list, contém a pontuação correta para cada resposta
        _destino: str, caminho para o arquivo que será gerado

    """
    arq = open(_arquivo,'r')
    line = arq.read()
    samples = line.split('\n')
    features = []

    for _, sample in enumerate(samples):
        if sample != "":
            # p = map(float, sample.split())
            p = [float(feature) for feature in sample.split()]
            features.append(p)

    data = {
        "features": np.array(features),
        "labels": np.array(_labels)
    }

    pickle.dump(data, open(_destino, "wb"))


def carrega_pickle(_arquivo):
    """ Método para carregar um arquivo pickle.

    Args:
        _arquivo: str, caminho para o arquivo pickle

    Returns:
        features: numpy array, contém os vetores das respostas
        labels: numpy array, contém a pontuação correta para cada resposta
    """
    data = pickle.load(open(_arquivo, "rb"))

    features = data["features"]
    labels = data["labels"]

    return features, labels


def report(cv_results_, n_top=3,arq=open('result','w')):
    """ Função para imprimir os resultados da busca pelos melhores parâmetros
    para classificadores.

    Args:
        grid_scores: scikit learn dict of numpy (masked) ndarrays, contém os
            scores de cada combinação testada
        n_top: int, quantia de resultados para imprimir

    """
    for i in range(n_top):

        mean = cv_results_["mean_test_score"][i]
        std = cv_results_["std_test_score"][i]
        params = cv_results_["params"][i]

        print("Combinacao: {0}".format(i + 1),file=arq)
        print("Performance media: {0:.3f} (std. deviation: {1:.3f})".format(
            mean, std),file=arq)
        print("Parâmetros: {0}\n".format(params),file=arq)
