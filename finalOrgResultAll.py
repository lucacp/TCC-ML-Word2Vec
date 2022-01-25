#encoding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import sys,logging,codecs
import operator
#from pprint import pprint

def ordena(medA):
    for j in range(len(medA)):
        for i in range(1,len(medA)):
            aux = medA[i]
            if medA[i-1][0] < medA[i][0]:
                medA[i]   = medA[i-1]
                medA[i-1] = aux
            else:
                if medA[i-1][0] == medA[i][0] and medA[i-1][1] > medA[i][1]:
                    medA[i]   = medA[i-1]
                    medA[i-1] = aux
    return
def transfResult(nm):
#
    arq  = codecs.open(nm,'r','utf-8')
    line = arq.read()
    line = line.replace('Buscando para algoritmo:', 'Buscando_para_algoritmo:,')
    line = line.replace( u'}'  , u',},')
    line = line.replace( u'{'  , u',{,')
    line = line.replace('std. deviation: ',',desvio_padrao:,')
    line = line.replace('Tempo de busca:',',Tempo_de_busca:,')
    line = line.replace(' secs para ','_secs_para_')
    line = line.replace(' candidatos.','_candidatos,')
    line = line.replace( '('  , '')
    line = line.replace( ')'  , ' ')
    line = line.replace( "'"  , '')
    line = line.replace( u'â'  , u'a')
    line = line.replace( '<class '  , '<class_')
    line = line.replace( 'Performance media: ','Performance_media:,')
    line = line.replace( '\n' , ',')
    line = line.replace( u' '  , u',')
    line = line.replace( '0.'  , '')
    line = line.replace( '\r'  , '')
    #
    vec  = ''
    flag = 0
    num  = 0
    numm = 0.0
    cont = 0
    alg  = []
    med  = 0.0
    desv = 0.0
    medA = {}
    arq.close()
    arq  = None
    #
    ar   = codecs.open('ordenado_'+nm,'w','utf-8')
    for x in line.split(','):
    #
        if flag > 0:
            if flag == 1: #
                vec   = vec + str(x)+'\n'
                alg.append(vec)
                vec   = None
                vec   = ''
                flag  = 0
                continue
            #    
            if flag == 2: #
                flag  = 0
                num   = x
                continue
            #
            if flag == 3:
                med   = int(x)
                flag  = 0
                continue
            #
            if flag == 4:
                desv  = int(x)
#
                flag  = 5
                continue   
            #
            if flag == 5:
                if x == '}':
                    vec        = vec + str(x)
                    #
                    medA[cont] = [med,desv,vec]
                    cont      += 1
                    vec        = None
                    vec        = '' 
                    flag       = 0
                    continue
                vec   = vec + str(x) + ' '
                continue
        #                
        else:    
            if x == 'Buscando_para_algoritmo:':
                vec = str(x)+' '
                #
                    #
                flag = 1
                continue
            #
            if x == 'Tempo_de_busca:':
                vec = str(x)+' '
                flag = 1
                continue
            #
            if x == 'Combinacao:':
                flag = 2
                continue
            #
            if x == 'Performance_media:':
                #
                flag = 3
                continue
            #
            if x == 'desvio_padrao:':
                #
                flag = 4
                continue
            
    ordena(medA)
    for i in range(len(medA)):
        print('Media: '+str(medA[i][0])+' Desvio_padrao: '+str(medA[i][1])+'\n'+medA[i][2],file=ar)
    ar.close()
    ar = None
#        
#ar   = None
#ar   = open(str(sys.argv[1]))
#
#tex  = ar.read()
#ar.close()
#ar   = None
#arqs = tex.split('\n')
#print('Result_soma_mc3s100w3.w2v-vec.txt')
#l    = 'Result_soma_mc3s100w3.w2v-vec.txt'
#transfResult(l)
#for i in arqs:
#    print('Result_soma_'+i+"-2-peso1.txt")
#    l='Result_soma_'+i+"-2-peso1.txt"
#    transfResult(l)
#    print('Result_soma_'+i+"-2-peso1-st.txt")
#    l='Result_soma_'+i+"-2-peso1-st.txt"
#    transfResult(l)
#    print('Result_soma_'+i+"-2-peso2.txt")
#    l='Result_soma_'+i+"-2-peso2.txt"
#    transfResult(l)
#    print('Result_soma_'+i+"-2-peso2-st.txt")
#    l='Result_soma_'+i+"-2-peso2-st.txt"
#    transfResult(l)
#    print('Result_soma_'+i+"-div.txt")
#    l='Result_soma_'+i+"-div.txt"
#    transfResult(l)
#    print('Result_soma_'+i+"-div-st.txt")
#    l='Result_soma_'+i+"-div-st.txt"
#    transfResult(l)
#    print('Result_soma_'+i+"-peso1.txt")
#    l='Result_soma_'+i+"-peso1.txt"
#    transfResult(l)
#    print('Result_soma_'+i+"-peso2.txt")
#    l='Result_soma_'+i+"-peso2.txt"
#    transfResult(l)
#    print('Result_soma_'+i+"-prob-st.txt")
#    l='Result_soma_'+i+"-prob-st.txt"
#    transfResult(l)
 #   print('Result_soma_'+i+"-vec.txt")
 #   l='Result_soma_'+i+"-vec.txt"
 #   transfResult(l)
 #   print('Result_soma_'+i+"-vec-st.txt")
 #   l='Result_soma_'+i+"-vec-st.txt"
 #   transfResult(l)
 #   print('Result_mult_'+i+"-mult.txt")
 #   l='Result_mult_'+i+"-mult.txt"
 #   transfResult(l)
 #   print('Result_mult_'+i+"-mult-st.txt")
 #   l='Result_mult_'+i+"-mult-st.txt"
 #   transfResult(l)
 #   print('Result_mult_'+i+"-multdiv.txt")
 #   l='Result_mult_'+i+"-multdiv.txt"
 #   transfResult(l)
 #   print('Result_mult_'+i+"-multdiv-st.txt")
 #   l='Result_mult_'+i+"-multdiv-st.txt"
 #   transfResult(l)

#    print('Result-Vec-SomaRed-gaussi_'+i+".txt")
#    l='Result-Vec-SomaRed-gaussi_'+i+".txt"
#    transfResult(l)
#    print('Result-Vec-SomaRed-gaussi_'+i+"-st.txt")
#    l='Result-Vec-SomaRed-gaussi_'+i+"-st.txt"
#    transfResult(l)

 #   print('Result-Vec-SomaRed-pca_n_'+i+".txt")
 #   l='Result-Vec-SomaRed-pca_n_'+i+".txt"
 #   transfResult(l)
 #   print('Result-Vec-SomaRed-pca_n_'+i+"-st.txt")
 #   l='Result-Vec-SomaRed-pca_n_'+i+"-st.txt"
 #   transfResult(l)

 #   print('Result-Vec-SomaRed-pca_w_'+i+".txt")
#    l='Result-Vec-SomaRed-pca_w_'+i+".txt"
#    transfResult(l)
#    print('Result-Vec-SomaRed-pca_w_'+i+"-st.txt")
#    l='Result-Vec-SomaRed-pca_w_'+i+"-st.txt"
#    transfResult(l)

 #   print('Result-Vec-SomaRed-sparse_'+i+".txt")
 #   l='Result-Vec-SomaRed-sparse_'+i+".txt"
 #   transfResult(l)
 #   print('Result-Vec-SomaRed-sparse_'+i+"-st.txt")
 #   l='Result-Vec-SomaRed-sparse_'+i+"-st.txt"
 #   transfResult(l)

 #   print('Result-spars_'+i+".txt")
 #   l='Result-spars_'+i+".txt"
 #   transfResult(l)
  #  print('Result-spars_'+i+"-st.txt")
  #  l='Result-spars_'+i+"-st.txt"
  #  transfResult(l)

#    print('Result-pca_w_'+i+".txt")
#    l='Result-pca_w_'+i+".txt"
#    transfResult(l)
#    print('Result-pca_w_'+i+"-st.txt")
#    l='Result-pca_w_'+i+"-st.txt"
#    transfResult(l)

 #   print('Result-pca_n_'+i+".txt")
 #   l='Result-pca_n_'+i+".txt"
 #   transfResult(l)
 #   print('Result-pca_n_'+i+"-st.txt")
 #   l='Result-pca_n_'+i+"-st.txt"
 #   transfResult(l)

  #  print('Result-gauss_'+i+".txt")
  #  l='Result-gauss_'+i+".txt"
  #  transfResult(l)
  #  print('Result-gauss_'+i+"-st.txt")
  #  l='Result-gauss_'+i+"-st.txt"
  #  transfResult(l)

#print('Result_soma_vectores.txt')
#l='Result_soma_vectores.txt'
#transfResult(l)

#l=[     "Result_soma__init-0.05_const-bias_2lr_hid100_proj0_vocab50000_batch1(20)_steps77(35)_maxNrm1.0_sgd-1.0_dec-12-0.5_dropout0.4vectores.txt",
#        "Result_soma__init-0.05_const-bias_2lr_hid100_proj0_vocab50000_batch1(24)_steps77(35)_maxNrm1.0_sgd-1.0_dec-12-0.5_dropout0.4vectores.txt",
#        "Result_soma__init-0.05_const-bias_2lr_hid100_proj0_vocab50000_batch1(30)_steps77(35)_maxNrm1.0_sgd-1.0_dec-12-0.5_dropout0.4vectores.txt",
#        "Result_soma__init-0.05_const-bias_2lr_hid100_proj0_vocab50000_batch1(20)_steps77(35)_maxNrm1.0_sgd-1.0_dec-12-0.5_dropout0.5vectores.txt",
#        "Result_soma__init-0.05_const-bias_2lr_hid100_proj0_vocab50000_batch1(24)_steps77(35)_maxNrm1.0_sgd-1.0_dec-12-0.5_dropout0.5vectores.txt",
#        "Result_soma__init-0.05_const-bias_2lr_hid100_proj0_vocab50000_batch1(30)_steps77(35)_maxNrm1.0_sgd-1.0_dec-12-0.5_dropout0.5vectores.txt",
#        "Result_soma__init-0.05_const-bias_2lr_hid100_proj0_vocab50000_batch1(20)_steps77(35)_maxNrm1.0_sgd-1.0_dec-12-0.5_dropout0.6vectores.txt",
#        "Result_soma__init-0.05_const-bias_2lr_hid100_proj0_vocab50000_batch1(24)_steps77(35)_maxNrm1.0_sgd-1.0_dec-12-0.5_dropout0.6vectores.txt",
#        "Result_soma__init-0.05_const-bias_2lr_hid100_proj0_vocab50000_batch1(30)_steps77(35)_maxNrm1.0_sgd-1.0_dec-12-0.5_dropout0.6vectores.txt",
#        "Result_soma__init-0.05_const-bias_2lr_hid125_proj0_vocab50000_batch1(20)_steps77(35)_maxNrm1.0_sgd-1.0_dec-12-0.5_dropout0.6vectores.txt"]

l=[     "Result_soma__init-0.05_const-bias_2lr_hid125_proj0_vocab50000_batch1(20)_steps77_maxNrm1.0_sgd-1.0_dec-12-0.5_dropout0.4vectores.txt",
        "Result_soma__init-0.05_const-bias_2lr_hid125_proj0_vocab50000_batch1(30)_steps77_maxNrm1.0_sgd-1.0_dec-12-0.5_dropout0.4vectores.txt",
        "Result_soma__init-0.05_const-bias_2lr_hid125_proj0_vocab50000_batch1(20)_steps77_maxNrm1.0_sgd-1.0_dec-12-0.5_dropout0.5vectores.txt",
        "Result_soma__init-0.05_const-bias_2lr_hid125_proj0_vocab50000_batch1(30)_steps77_maxNrm1.0_sgd-1.0_dec-12-0.5_dropout0.5vectores.txt",
        "Result_soma__init-0.05_const-bias_2lr_hid125_proj0_vocab50000_batch1(30)_steps77_maxNrm1.0_sgd-1.0_dec-12-0.5_dropout0.6vectores.txt"]

for i in l:
    print(i)
    transfResult(i)