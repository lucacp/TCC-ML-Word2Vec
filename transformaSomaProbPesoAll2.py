#encoding: utf-8
import sys,logging
from pprint import pprint

def transfSomaProbp(nm):
#    nm   = str(sys.argv[1])
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
    #y    = ''
    num  = 0
    arq.close()
    arq  = None
    ar   = open('soma_'+nm,'w')
    #print(line)
    for x in line.split(','):
    #    print(x)
        if x == 'None':
            if num > 0:
                num = 0
                vec = vec + '\n'
                ar.write(vec)
        else:
            if x == 'dtypefloat32':
                vec = vec + '\n'
                ar.write(vec)
                num = 0
            else:    
                if x == 'array':
                    if num > 0:
                        vec = vec + '\n'
                        ar.write(vec)
                    num += 1 
                    vec  = None
                    vec  = ''
                else:
                    #if num != 0:
                        #vec=vec+str(x)+' '
                    #else:
                        #y=y+str(x)+' '
                    vec = vec + str(x) + ' '
    #print(vec)
    #print(y)
    if num > 0:
        ar.write(vec)#+y)
    ar.close()
    ar = None
ar   = None
ar   = open(str(sys.argv[1]))
#dados=str(sys.argv[2])
tex  = ar.read()
ar.close()
ar   = None
arqs = tex.split('\n')
for i in arqs:
    l=None
    print(i + "-2-peso1.txt")
    l = i + "-2-peso1.txt"
    transfSomaProbp(l)
    l=None
    print(i + "-2-peso2.txt")
    l = i + "-2-peso2.txt"
    transfSomaProbp(l)
    l=None
    print(i + "-2-peso1-st.txt")
    l = i + "-2-peso1-st.txt"
    transfSomaProbp(l)
    l=None
    print(i + "-2-peso2-st.txt")
    l = i + "-2-peso2-st.txt"
    transfSomaProbp(l)
    l=None
#