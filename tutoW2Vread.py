import os, sys
import gensim, logging
from gensim.models import Word2Vec
from pprint import pprint
import codecs
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

nmvc = str(sys.argv[1])
model = Word2Vec.load(nmvc)
model.init_sims(replace=True)
#pprint(model.wv.vocab)
arq = codecs.open("treinamento"+nmvc+".txt",'w','utf-8')
pprint(model.wv.vocab,arq)
arq.close()
