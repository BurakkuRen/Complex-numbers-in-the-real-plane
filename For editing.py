import numpy as np
import matplotlib.pyplot as plt
import itertools

import time #to see how long it takes
start_time = time.time()
print("process started at: %s"%(start_time))

real = [] #contiene la parte real de las raíces, la perteneciente al eje x
imag = [] #contiene la parte imaginaria de las raíces, la perteneciente al eje y
roots = {} #||||||||||| una lista de todas las raíces obtenidas, para quitar duplicados. |||||||||||

#cada índice de las listas arriba corresponde a un polinomio y las partes real e imaginaria de una de sus raíces
#los polinomios que tengan más de una raíz aparecerán varias veces

rows = 1 #cambiar de acuerdo a la cantidad de gráficas a mostrar. 
cols = 5 #cambiar de acuerdo a la cantidad de gráficas a mostrar. 
fig, ax = plt.subplots(rows, cols)

grado = 4 #grado máximo de los polinomios
valorCoef =5 #los coeficientes tomarán valores en el rango [-valorCoef, valorCoef]

rangoCoef = [x for x in range(-valorCoef,valorCoef+1)] 
coeficients = list(itertools.product(rangoCoef, repeat=grado+1))
print("--- %s seconds ---" %(time.time()-start_time))
#creamos un polinomio con cada una de las posibles combinaciones de coeficientes,
#lo solucionamos, y añadimos las partes real e imaginaria de todas sus raíces a la lista correspondiente,
#junto con la combinación de coeficientes usada para obtener esa raíz
coeficients.sort(key=lambda coord: tuple(float("inf") if x==0 else x for x in coord))
#the above can also be achieved with key=lambda x: tuple((n!=0,n) for n in x),
#y organiza los polinomios de forma que aquellos que empiecen por 0 sean los úñtimos, para poder separarlos por grado
#0 goes last, otherwise ascending
print("--- %s seconds ---" %(time.time()-start_time))
for comb in coeficients:
    p = np.poly1d(comb)
    root = p.r
    for n in root:
        roots[n] = comb
    
print("--- %s seconds ---" %(time.time()-start_time))

#creamos una lista de listas con una cantidad de elementos igual al máximo grado generado 
dg = []
for _ in range(grado):
    dg.append([])

#agrupamos todas las raíces en grupos según el grado del polinomio que solucionan
#las colocamos en dg de mayora menor: 
#dg[-1] = polinomios de grado máximo, dg[0] = polinomios de grado mínimo

for i in roots:
    for ind, coef in enumerate(roots[i],1): #si ind = 0, el grado es el mayor posible 
        if coef != 0:
            dg[grado-ind].append(i)
            break
print("--- %s seconds ---" %(time.time()-start_time))


################### find  the two closest numbers to searchNum, ####################################################################################################################
################### should be upgraded so as to find the 20 (for example) closest numbers, 10 above it and 10 below it, otherwise, it will be troublesome ##########################
################### another line of code can be added to, whithin those 20 closest, compare them number by number, #################################################################
###################and find the closes one/two #####################################################################################################################################
"""searchNum = 1.5+0.866j
for i, v in enumerate(dg):
    sortedV = np.sort_complex(v)
    print(sortedV)
    print(sortedV[bisect_left(sortedV,searchNum)], sortedV[bisect_left(sortedV,searchNum)-1])
    print(1 in sortedV)
    print(any([x in dg[i+1] for x in sortedV]))"""


################### Proof that all roots of polinomials degree x #######################################
################### contain all roots of polinomials degree y, when y<x ################################
################### disable the part of the code that gets rid of duplicates to test ###################
"""
c= 1
co = 0
for l in dg:
    q = [real[x] for x in l]
    r = [imag[x] for x in l]
    ql = [real[x] for x in dg[-1]]
    rl = [imag[x] for x in dg[-1]]
    
    if all(x in ql for x in q):
        print("all REALS contained for degree %s"%(c))

    if all(x in rl for x in r):
        print("all IMAGS contained for degree %s"%(c))
    c+=1
"""
#representamos todas las raíces procedentes de cada grado de mayor grado a menor para que las grandes
#no tapen las pequeñas
for i in range(1,grado+1):
    ax[4].plot([np.real(x) for x in dg[grado-i]], [np.imag(x) for x in dg[grado-i]], "o", markersize=1,label="g%s"%(str(grado-i+1)))

ax[0].plot([np.real(x) for x in dg[0]], [np.imag(x) for x in dg[0]], "o", markersize=1,label="g%s"%(str(grado-i+1)))
ax[1].plot([np.real(x) for x in dg[1]], [np.imag(x) for x in dg[1]], "go", markersize=1,label="g%s"%(str(grado-i+1)))
ax[2].plot([np.real(x) for x in dg[2]], [np.imag(x) for x in dg[2]], "ro", markersize=1,label="g%s"%(str(grado-i+1)))
ax[3].plot([np.real(x) for x in dg[3]], [np.imag(x) for x in dg[3]], "bo", markersize=1,label="g%s"%(str(grado-i+1)))

for i, b in enumerate(ax,1):
    b.axis("equal")
    b.legend()
    b.add_artist(plt.Circle((0,0),1,color="#000000",fill=False))
    b.set_title("Grado %s"%(i)) if i != grado+1 else b.set_title("Grado 1-%s"%(grado))

print("--- %s seconds ---" %(time.time()-start_time))
plt.show()
