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
    num = 0
    arq.close()
    arq=None
    ar = open('Vec-'+nm,'w')
    for x in line.split(','):
        #print(x)
        if x == 'dtypefloat32':
            
            #vec=vec+'\n'
            #ar.write(vec)
            #vec = None
            #vec = ''
            if num >= 63:
                vec = None
                vec = ''
        else:
            if x == 'array':
                #num=1
                if num > 0:
                    vec=vec+'\n'
                ar.write(vec)
                vec = None
                vec = ''
                num += 1
                #num = 0
            else:
                #if num != 0:
                    #vec=vec+str(x)+' '
                #else:
                    #y=y+str(x)+' '
                vec=vec+str(x)+' '
                
    #print(vec)
    #print(y)
    ar.write(vec+'\n')#+y)
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
    print('SomaConcat-gaussi_'+i+".txt")
    l='SomaConcat-gaussi_'+i+".txt"
    transfConcat(l)
    l=None
    print('SomaConcat-gaussi_'+i+"-st.txt")
    l='SomaConcat-gaussi_'+i+"-st.txt"
    transfConcat(l)
    l=None
    print('SomaConcat-pca_n_'+i+".txt")
    l='SomaConcat-pca_n_'+i+".txt"
    transfConcat(l)
    l=None
    print('SomaConcat-pca_n_'+i+"-st.txt")
    l='SomaConcat-pca_n_'+i+"-st.txt"
    transfConcat(l)
    l=None
    print('SomaConcat-pca_w_'+i+"-st.txt")
    l='SomaConcat-pca_w_'+i+"-st.txt"
    transfConcat(l)
    l=None
    print('SomaConcat-pca_w_'+i+".txt")
    l='SomaConcat-pca_w_'+i+".txt"
    transfConcat(l)
    l=None
    print('SomaConcat-sparse_'+i+".txt")
    l='SomaConcat-sparse_'+i+".txt"
    transfConcat(l)
    l=None
    print('SomaConcat-sparse_'+i+"-st.txt")
    l='SomaConcat-sparse_'+i+"-st.txt"
    transfConcat(l)
    l=None
    