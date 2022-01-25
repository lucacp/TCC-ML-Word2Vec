#encoding: utf-8
# import modules & set up logging
import os
import gensim, logging
from pprint import pprint
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
 
#sentences = [['first', 'sentence'], ['second', 'sentence']]
# train word2vec on the two sentences
#model = gensim.models.Word2Vec(sentences, min_count=1)

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                line=line.replace(","," ")
                line=line.replace("."," ")
                line=line.replace("'"," ")
                line=line.replace('"'," ")
                line=line.replace(">"," ")
                line=line.replace("<"," ")
                line=line.replace(";"," ")
                line=line.replace("="," ")
                line=line.replace("!"," ")
                line=line.replace("?"," ")
                line=line.replace("("," ")
                line=line.replace(")"," ")
                line=line.replace(":"," ")
                line=line.replace("#"," ")
                line=line.lower()
                line=line.replace(u"á".encode('utf-8'),"a")
                line=line.replace(u"à".encode('utf-8'),"a")
                line=line.replace(u"ã".encode('utf-8'),"a")
                line=line.replace(u'â'.encode('utf-8'),"a")
                line=line.replace(u"ä".encode('utf-8'),"a")
                line=line.replace(u"é".encode('utf-8'),"e")
                line=line.replace(u"è".encode('utf-8'),"e")
                line=line.replace(u"ê".encode('utf-8'),"e")
                line=line.replace(u"ë".encode('utf-8'),"e")
                line=line.replace(u"í".encode('utf-8'),"i")
                line=line.replace(u"ì".encode('utf-8'),"i")
                line=line.replace(u'î'.encode('utf-8'),"i")
                line=line.replace(u"ï".encode('utf-8'),"i")
                line=line.replace(u"ó".encode('utf-8'),"o")
                line=line.replace(u"ò".encode('utf-8'),"o")
                line=line.replace(u"õ".encode('utf-8'),"o")
                line=line.replace(u'ô'.encode('utf-8'),"o")
                line=line.replace(u"ö".encode('utf-8'),"o")
                line=line.replace(u"ú".encode('utf-8'),"u")
                line=line.replace(u"ù".encode('utf-8'),"u")
                line=line.replace(u"û".encode('utf-8'),"u")
                line=line.replace(u'ü'.encode('utf-8'),"u")
                line=line.replace(u"ç".encode('utf-8'),"c")
                yield line.split()
 
sentences = MySentences('c:\ice1life\pt_BR.raw\GNOME\pt_BR\w2v') # a memory-friendly iterator
model = gensim.models.Word2Vec(sentences,iter=1,min_count=5)
model.save("testew2v-p5")
model = None
#sentences2 = MySentences('c:\ice1life\pt_BR.raw\GNOME\pt_BR\w2vtest') # a memory-friendly iterator
#model = gensim.models.Word2Vec(sentences2,iter=1)  # an empty model, no training yet
#model.build_vocab(sentences2)  # can be a non-repeatable, 1-pass generator
#model.train(sentences)  # can be a non-repeatable, 1-pass generator
#model.save("testew2v-p4")
#model = None
#print(model.wv.vocab())
#pprint(model.wv.vocab)
#model['baixar']
#model = Word2Vec(sentences, workers=4)
#model = Word2Vec.load