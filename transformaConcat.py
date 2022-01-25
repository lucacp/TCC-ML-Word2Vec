#encoding: utf-8
import sys,logging
from pprint import pprint

nm=str(sys.argv[1])
arq=open(nm,'r')
line=arq.read()
line=line.replace('array','array,')
line=line.replace('[','')
line=line.replace(']','')
#line=line.replace('(','')
#line=line.replace(')','')
#line=line.replace('=','')
#line=line.replace(' ','')
line=line.replace('\n',' ')
vec=''
#y=''
num=0
arq.close()
arq=None
ar = open('concat_'+nm,'w')
for lin in line.split('\n'):
    for x in lin.split(' '):
#    print(x)
        if x == '#' and num != 0:
            num = 0
            vec=vec+'\n'
            ar.write(vec)
            vec = None
            vec = ''
        else:
            if x == '#':
                num = 0
                #vec=vec+'\n'
            else:
                num=1
                vec=vec+str(x)+' '
            
#print(vec)
#print(y)
#ar.write(vec+'\n')#+y)
ar.close()
ar = None
