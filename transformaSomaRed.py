#encoding: utf-8
import sys,logging
from pprint import pprint

def transfSomaRed(nm):
    #nm=str(sys.argv[1])
    arq  = open(nm,'r')
    line = arq.read()
    line = line.replace('array','array,')
    line = line.replace('[','')
    line = line.replace(']','')
    line = line.replace('(','')
    line = line.replace(')','')
    line = line.replace('=','')
    line = line.replace(' ','')
    line = line.replace('\n',',')
    vec  = ''
    #y=''
    num  = 1
    arq.close()
    arq=None
    flag = 0
    ar = open('Vec-'+nm,'w')
    for x in line.split(','):
        #print(x)
        if x == 'dtypefloat32':
            if flag != 2:
                flag = 1
                
        else:
            if x == 'array':
                #num=1
                if num > 1:
                    vec=vec+'\n'
                    ar.write(vec)
                    if flag == 0:
                        flag = 2
                vec  = None
                vec  = ''
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
    if flag > 0:
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
    print('SomaRed-gaussi_'+i+".txt")
    l='SomaRed-gaussi_'+i+".txt"
    transfSomaRed(l)
    l=None
    print('SomaRed-gaussi_'+i+"-st.txt")
    l='SomaRed-gaussi_'+i+"-st.txt"
    transfSomaRed(l)
    l=None
    print('SomaRed-pca_n_'+i+".txt")
    l='SomaRed-pca_n_'+i+".txt"
    transfSomaRed(l)
    l=None
    print('SomaRed-pca_n_'+i+"-st.txt")
    l='SomaRed-pca_n_'+i+"-st.txt"
    transfSomaRed(l)
    l=None
    print('SomaRed-pca_w_'+i+".txt")
    l='SomaRed-pca_w_'+i+".txt"
    transfSomaRed(l)
    l=None
    print('SomaRed-pca_w_'+i+"-st.txt")
    l='SomaRed-pca_w_'+i+"-st.txt"
    transfSomaRed(l)
    l=None
    print('SomaRed-sparse_'+i+".txt")
    l='SomaRed-sparse_'+i+".txt"
    transfSomaRed(l)
    l=None
    print('SomaRed-sparse_'+i+"-st.txt")
    l='SomaRed-sparse_'+i+"-st.txt"
    transfSomaRed(l)
    l=None
    