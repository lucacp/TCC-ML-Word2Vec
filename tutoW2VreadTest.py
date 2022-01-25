import os
import gensim, logging
from gensim.models import Word2Vec
from pprint import pprint
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
mo=None
mo = Word2Vec.load("testew2v-p5")
mo.init_sims(replace=True)
#pprint(model.wv.vocab)
print(mo.most_similar(positive=['mulher','rei','coroa'],negative=['homem']))#rainha,princesa
print(mo.most_similar(positive=['japao','desenho'],negative=['pais']))#manga,anime
print(mo.most_similar(positive=['japao','brasilia'],negative=['brasil']))#toquio
print(mo.most_similar(positive=['colombia','paris'],negative=['franca']))#bogota
print(mo.most_similar(positive=['portugal','paris'],negative=['franca']))#lisboa

#mo.most_similar(positive=['mulher','rei','coroa'],negative=['homem'])#rainha,princesa
#mo.most_similar(positive=['mulher','rei','coroa'],negative=['homem'])#rainha,princesa
#mo.most_similar(positive=['mulher','rei','coroa'],negative=['homem'])#rainha,princesa
#mo.most_similar(positive=['mulher','rei','coroa'],negative=['homem'])#rainha,princesa
#mo.most_similar(positive=['mulher','rei','coroa'],negative=['homem'])#rainha,princesa
#mo.most_similar(positive=['mulher','rei','coroa'],negative=['homem'])#rainha,princesa
#mo.most_similar(positive=['mulher','rei','coroa'],negative=['homem'])#rainha,princesa
#mo.most_similar(positive=['mulher','rei','coroa'],negative=['homem'])#rainha,princesa
#mo.most_similar(positive=['mulher','rei','coroa'],negative=['homem'])#rainha,princesa
#mo.most_similar(positive=['mulher','rei','coroa'],negative=['homem'])#rainha,princesa
#mo.most_similar(positive=['mulher','rei','coroa'],negative=['homem'])#rainha,princesa
#mo.most_similar(positive=['mulher','rei','coroa'],negative=['homem'])#rainha,princesa
