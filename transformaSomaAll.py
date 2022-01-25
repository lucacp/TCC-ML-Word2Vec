#encoding: utf-8
import sys,logging
from pprint import pprint

def transfSoma(nm):
#    nm=str(sys.argv[1])
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
    ar = open('soma_'+nm,'w')
    #print(line)
    for x in line.split(','):
    #    print(x)
        if x == 'None':
            num = 0
            vec=vec+'\n'
        else:
            if x == 'dtypefloat32':
                num = 0
                vec=vec+'\n'
                ar.write(vec)
                vec = None
                vec = ''
            else:
                if x == 'array':
                    num=1
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
    #print(i+"-vec.txt")
    #l=i+"-vec.txt"
    #transfSoma(l)
    print(i+"-vec-st.txt")
    l=i+"-vec-st.txt"
    transfSoma(l)
