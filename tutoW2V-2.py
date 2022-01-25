#encoding: utf-8
# import modules & set up logging
import os
import gensim, logging
from pprint import pprint
import multiprocessing
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
                line=line.replace("["," ")
                line=line.replace("]"," ")
                line=line.replace("´","")
                line=line.replace("`","")
                line=line.replace("{"," ")
                line=line.replace("}"," ")
                line=line.replace("¨"," ")
                line=line.replace("&"," ")
                line=line.replace("@"," ")
                line=line.replace("¬"," ")
                line=line.lower()
                line=line.replace("á","a")
                line=line.replace("à","a")
                line=line.replace("ã","a")
                line=line.replace('â',"a")
                line=line.replace("ä","a")
                line=line.replace("é","e")
                line=line.replace("è","e")
                line=line.replace("ê","e")
                line=line.replace("ë","e")
                line=line.replace("í","i")
                line=line.replace("ì","i")
                line=line.replace('î',"i")
                line=line.replace("ï","i")
                line=line.replace("ó","o")
                line=line.replace("ò","o")
                line=line.replace("õ","o")
                line=line.replace('ô',"o")
                line=line.replace("ö","o")
                line=line.replace("ú","u")
                line=line.replace("ù","u")
                line=line.replace("û","u")
                line=line.replace('ü',"u")
                line=line.replace("ç","c")
                line=line.decode('utf-8')
                line=line.encode('ascii', 'ignore')
                yield line.split()
sentences = MySentences('c:\ice1life\pt_BR.raw\GNOME\pt_BR\w2v') # a memory-friendly iterator
erou=[]
mcsw="mc3s3w3"
try:
    model = gensim.models.Word2Vec(sentences,iter=1,min_count=3,size=300,window=3,workers=multiprocessing.cpu_count())
    model.save(mcsw)
except:
    print(mcsw)
    erou.append(mcsw)
model = None
mcsw = None
mcsw="mc3s3w5"
try:
    model = gensim.models.Word2Vec(sentences,iter=1,min_count=3,size=300,window=5,workers=multiprocessing.cpu_count())
    model.save(mcsw)
except:
    print(mcsw)    
    erou.append(mcsw)
model = None
mcsw = None
mcsw = "mc3s3w7"
try:
    model = gensim.models.Word2Vec(sentences,iter=1,min_count=3,size=300,window=7,workers=multiprocessing.cpu_count())
    model.save(mcsw)
except:
    print(mcsw)    
    erou.append(mcsw)
model = None
mcsw = None
mcsw = "mc3s2w3"
try:
    model = gensim.models.Word2Vec(sentences,iter=1,min_count=3,size=200,window=3,workers=multiprocessing.cpu_count())
    model.save(mcsw)
except:
    print(mcsw)    
    erou.append(mcsw)
model = None
mcsw = None
mcsw="mc3s2w5"
try:
    model = gensim.models.Word2Vec(sentences,iter=1,min_count=3,size=200,window=5,workers=multiprocessing.cpu_count())
    model.save(mcsw)
except:
    print(mcsw)
    erou.append(mcsw)
model = None
mcsw = None
mcsw = "mc3s2w7"
try:
    model = gensim.models.Word2Vec(sentences,iter=1,min_count=3,size=200,window=7,workers=multiprocessing.cpu_count())
    model.save(mcsw)
except:
    print(mcsw)
    erou.append(mcsw)
model = None
mcsw = None
mcsw = "mc3s1w3"
try:
    model = gensim.models.Word2Vec(sentences,iter=1,min_count=3,size=100,window=3,workers=multiprocessing.cpu_count())
    model.save(mcsw)
except:
    erou.append(mcsw)
    print(mcsw)
model = None
mcsw = None
mcsw = "mc3s1w5"
try:
    model = gensim.models.Word2Vec(sentences,iter=1,min_count=3,size=100,window=5,workers=multiprocessing.cpu_count())
    model.save(mcsw)
except:
    print(mcsw)
    erou.append(mcsw)
model = None
mcsw = None
mcsw = "mc3s1w7"
try:
    model = gensim.models.Word2Vec(sentences,iter=1,min_count=3,size=100,window=7,workers=multiprocessing.cpu_count())
    model.save(mcsw)
except:
    print(mcsw)
    erou.append(mcsw)
model = None
mcsw = None
mcsw = "mc5s1w3"
try:
    model = gensim.models.Word2Vec(sentences,iter=1,min_count=5,size=100,window=3,workers=multiprocessing.cpu_count())
    model.save(mcsw)
except:
    print(mcsw)
    erou.append(mcsw)
model = None
mcsw = None
mcsw = "mc5s2w3"
try:
    model = gensim.models.Word2Vec(sentences,iter=1,min_count=5,size=200,window=3,workers=multiprocessing.cpu_count())
    model.save(mcsw)
except:
    print(mcsw)
    erou.append(mcsw)
model = None
mcsw = None
mcsw = "mc5s3w3" 
try:
    model = gensim.models.Word2Vec(sentences,iter=1,min_count=5,size=300,window=3,workers=multiprocessing.cpu_count())
    model.save(mcsw)
except:
    print(mcsw)
    erou.append(mcsw)
model = None
mcsw = None
mcsw = "mc5s1w5"
try:
    model = gensim.models.Word2Vec(sentences,iter=1,min_count=5,size=100,window=5,workers=multiprocessing.cpu_count())
    model.save(mcsw)
except:
    print(mcsw)
    erou.append(mcsw)
model = None
mcsw = None
mcsw = "mc5s2w5"
try:
    model = gensim.models.Word2Vec(sentences,iter=1,min_count=5,size=200,window=5,workers=multiprocessing.cpu_count())
    model.save(mcsw)
except:
    print(mcsw)
    erou.append(mcsw)
model = None
mcsw = None
mcsw = "mc5s3w5"
try:
    model = gensim.models.Word2Vec(sentences,iter=1,min_count=5,size=300,window=5,workers=multiprocessing.cpu_count())
    model.save(mcsw)
except:
    print(mcsw)
    erou.append(mcsw)
model = None
mcsw = None
mcsw = "mc5s1w7"
try:
    model = gensim.models.Word2Vec(sentences,iter=1,min_count=5,size=100,window=7,workers=multiprocessing.cpu_count())
    model.save(mcsw)
except:
    print(mcsw)
    erou.append(mcsw)
model = None
mcsw = None
mcsw = "mc5s2w7"
try:
    model = gensim.models.Word2Vec(sentences,iter=1,min_count=5,size=200,window=7,workers=multiprocessing.cpu_count())
    model.save(mcsw)
except:
    print(mcsw)
    erou.append(mcsw)
model = None
mcsw = None
mcsw="mc5s3w7"
try:
    model = gensim.models.Word2Vec(sentences,iter=1,min_count=5,size=300,window=7,workers=multiprocessing.cpu_count())
    model.save(mcsw)
except:
    print(mcsw)    
    erou.append(mcsw)
model = None
mcsw = None
print(erou)
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