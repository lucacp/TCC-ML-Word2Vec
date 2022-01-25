#encoding: utf-8
"""
Tutorial para execução de k-fold cross-validation e grid-search.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import sys
from gensim.models import Word2Vec
from sklearn.decomposition import IncrementalPCA
from sklearn.random_projection import GaussianRandomProjection
from sklearn.random_projection import SparseRandomProjection

# pylint: disable = C0103

# algumas 'respostas' só pra ter um exemplo
# quando estiver executando com as respostas originais, terás que gerar as
# matrizes como está ali em baixo
resposta01 = "o ceu e azul"
resposta02 = "o sol e amarelo quando brilha"

respostas = [resposta01, resposta02]

#  carregando os vetores aprendidos na wikipedia
#model = "/home/gian/python/correcao_automatica/models/mc5s100w3/mc5s100w3.w2v"
model = str(sys.argv[1])
w2v = Word2Vec.load(model)

# obtendo as respostas
# como estou usando respostas inventadas, tive que incluir esta parte
# no caso se já tiver as respostas colocadas como os vetores, pode pular as
# próximas linhas
matrizes = []
for resposta in respostas:

  palavras = resposta.split()
  vetores = []

  for token in palavras:
    vetor = w2v.wv[token]
    shape0 = vetor.shape[0]
    vetores.append(vetor.reshape(shape0, 1))

  vetores = np.concatenate(vetores, axis=1)
  matrizes.append(vetores)

# aqui definimos os PCAs, e as projeções Gaussiana e Esparsa
# note-se que vamos usar apenas o 'primeiro componente' do resultado de cada
# um. Nós poderíamos ter mais do que um componente, mas dai seria 1 vetor para
# cada componente e teriamos então que combinar estes vetores. Por isso ficamos
# apenas com o primeiro (que melhor representa os dados).

# para o PCA vamos usar 2 tipos: o padrão e um com whitening
# whitening vai transformar a matriz antes de aplciar o PCAs
# vamos ver como os se comportam então testamos com os 2
pca_regular = IncrementalPCA(n_components=1, whiten=False)
pca_whiten = IncrementalPCA(n_components=1, whiten=True)
# para as projeções vale a mesma coisa do primeiro componente
gaussian_projection = GaussianRandomProjection(n_components=1)
sparse_projection = SparseRandomProjection(n_components=1)

# listas que vão armazenar as novas representações das respostas geradas pelo
# métodos acima. cada lista destas vai conter um novo vetor para cada resposta.
# cada novo vetor vai ser uma forma combinada dos vetores das palavras que
# compõem as respostas. a diferença é que ao invés de fazer uma soma, vamos
# aplicar redução ou projeção.
# como estes novos vetores, podemos usar o mesmo script/métodos para a busca
# dos parâmetros que utilizamos para testar as somas.
respostas_pca_regular = []
respostas_pca_whiten = []
respostas_gaussian_projection = []
respostas_sparse_projection = []

for matriz in matrizes:

  # aqui temos que aplicar para cada resposta os métodos pois cada matriz
  # será diferente e os métodos são baseados na própria matriz. não teria
  # sentido aplicar a mesma coisa para todas elas

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
#
print(respostas_pca_regular)
print('\n')
print(respostas_pca_whiten)
print('\n')
print(respostas_gaussian_projection)
print('\n')
print(respostas_sparse_projection)
