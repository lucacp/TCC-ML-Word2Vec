#encoding: utf-8
import sys,logging
from pprint import pprint

def transfConcat(nm):
    #nm=str(sys.argv[1])
    arq=open(nm,'r')
    line=arq.read()
    line=line.replace('array','array,')
    line=line.replace('[','')
    line=line.replace(']','')
    line=line.replace('(','')
    line=line.replace(')','')
    line=line.replace('=','')
    line=line.replace(' ','')
    line=line.replace('\n',',')
    vec=''
    #y=''
    num=0
    arq.close()
    arq=None
    ar = open('Vec-'+nm,'w')
    for x in line.split(','):
        #print(x)
        if x == 'None':
            #num = 0
            vec=vec+'\n'
        else:
            if x == 'dtypefloat32':
                num = 0
                #vec=vec+'\n'
                #ar.write(vec)
                #vec = None
                #vec = ''
            else:
                if x == 'array':
                    #num=1
                    vec=vec+'\n'
                    ar.write(vec)
                    vec = None
                    vec = ''
                else:
                    #if num != 0:
                        #vec=vec+str(x)+' '
                    #else:
                        #y=y+str(x)+' '
                    vec=vec+str(x)+' '
                
    #print(vec)
    #print(y)
    #ar.write(vec+'\n')#+y)
    ar.close()
    ar = None
ar=None
ar=open(str(sys.argv[1]))
#dados=str(sys.argv[2])
tex=ar.read()
ar.close()
ar=None
arqs=tex.split('\n')
for i in arqs:
    print('Concat_-gaussi_'+i+".txt")
    l='Concat_-gaussi_'+i+".txt"
    transfConcat(l)
    l=None
    print('Concat_-gaussi_'+i+"-st.txt")
    l='Concat_-gaussi_'+i+"-st.txt"
    transfConcat(l)
    l=None
    print('Concat_-pca_n_'+i+".txt")
    l='Concat_-pca_n_'+i+".txt"
    transfConcat(l)
    l=None
    print('Concat_-pca_n_'+i+"-st.txt")
    l='Concat_-pca_n_'+i+"-st.txt"
    transfConcat(l)
    l=None
    print('Concat_-pca_w_'+i+"-st.txt")
    l='Concat_-pca_w_'+i+"-st.txt"
    transfConcat(l)
    l=None
    print('Concat_-pca_w_'+i+".txt")
    l='Concat_-pca_w_'+i+".txt"
    transfConcat(l)
    l=None
    print('Concat_-sparse_'+i+".txt")
    l='Concat_-sparse_'+i+".txt"
    transfConcat(l)
    l=None
    print('Concat_-sparse_'+i+"-st.txt")
    l='Concat_-sparse_'+i+"-st.txt"
    transfConcat(l)
    l=None
    