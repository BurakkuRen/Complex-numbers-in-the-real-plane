import numpy as np
import itertools
import multiprocessing as mp

import time #to see how long it takes
start_time = time.time()
print("16:59")


#se calcularán todas las raíces de grado 1 a grado maxDg con coeficientes desde [-1,1]
#hasta [-maxCoef,maxCoef]


#generamos y solucionamos los polinomios
def generateAndSolve(grado, valorCoef):
    rangoCoef = [x for x in range(-valorCoef,valorCoef+1)]

    #creamos una lista que tenga todas las combinaciones posibles de longitud grado y posibles valores rangoCoef
    #la longitud es 1 menos de la adecuada, pero se añade luego
    #lo hacemos así para que no ponga 0 en la posición inicial, y además, reduce drásticamente la longitud de la lista
    coeficientes = list(itertools.product(rangoCoef, repeat=grado))

    roots = set()

    #iteramos por todos los valores en rangoCoef ignorando el 0. estos valores (i) serán el coeficiente del primer elemento
    #por eso no pueden ser 0. generamos y solucionamos los polinomios y añadimos las raíces a roots. 
    #por último devolvemos el set con las raíces. Usamos un set para evitar la presencia de duplicados
    rangoCoef.remove(0)
    for i in rangoCoef:
        for comb in coeficientes:
            p = np.poly1d([i]+list(comb))
            for n in p.r:
                roots.add(n)
    return roots

#añadimos al dicionario un nuevo valor con llave g(grado) con las raíces que surgen
#al ejecutar la generación de polinomios con ese grado y coeficientes
def addDegree(finalDict,dg,coef):
    finalDict["g%s"%(dg)] = generateAndSolve(dg,coef)
    print("subprocess %s (%s) has ended in %s seconds"%(dg, __name__, time.time()-start_time))

def main():
    global finalDict #me he visto forzado, si no daba error

    #para cada rango de coeficientes generamos una serie de procesos 
    #que ejecuten la función addDegree con todos los grados entre 1 y el máximo
    #estos procesos se ejecutarán al mismo tiempo para maximizar el processing power del ordenador 
    #y minimizar el tiempo que tarda en ejecutarse el programa.
    for coef in range(1,maxCoef+1):
        for dg in range(1,maxDg+1):
            processes.append(mp.Process(target=addDegree, args=(finalDict,dg,coef)))

        for p in processes:
            p.start()

        #esperamos a que termine el último proceso (el más largo, pues tiene el mayor grado), 
        #y decspués reseteamos la lista de procesos para que no de problemas en el siguiente loop 
        processes[-1].join()
        processes.clear()
        print("------- %s seconds -------"%(time.time()-start_time))

        #cambiamos el tipo del finalDict a el de un diccionario normal de python
        #en vez de uno de manager.dict(), y creamos una lista inversa con los
        #valores entre el grado máximo y 1.
        finalDict = dict(finalDict)
        dgRange = [x for x in range(maxDg,0,-1)]

        #dado que las raíces de grado 5 contienen las de grado 4, podemos liberar espacio
        #quitando las raíces que coinciden. para conseguirlo, a cada grupo de raíces le quitamos el grupo inmediatamente inferior
        #por último, los valores presentes en el diccionario son raíces completas, lo cual no nos sirve,
        #por lo que las pasamos a una lista de listas donde las sublistas contienen los valores real e imaginario de cada raíz
        #guardamos el diccionario en un archivo cuyo nombre indique que valores contiene, limpiamos el diccionario para
        #liberar espacio y volvemos a pasar finalDict a un diccionario de tipo manager.dict()
        for i in dgRange:
            if i != 1:
                finalDict["g%s"%(i)] -= finalDict["g%s"%(i-1)]
            finalDict["g%s"%(i)] = [[np.real(x) for x in finalDict["g%s"%(i)]],[np.imag(x) for x in finalDict["g%s"%(i)]]]
        print("------- %s seconds -------"%(time.time()-start_time))
        np.save("./Roots/Coeficientes_%s"%(coef),finalDict)
        finalDict.clear()
        finalDict = manager.dict()

#creamos un objeto multiprocessing.Manager() para poder crear un diccionario que los distintos procesos sean capaces de editar,
#llamamos main(), y cuando acabe el proceso printeamos el tiempo transcurrido.
if __name__ == "__main__": #comprobación necesaria por multiprocessing
    maxDg = 12
    maxCoef = 1
    processes = []
    
    manager = mp.Manager()
    finalDict = manager.dict()
    try:
        main()
    except:
        print("FAILED")
        print("------- %s seconds -------"%(time.time()-start_time))

    print("------- %s seconds -------"%(time.time()-start_time))



##################For some reason, it's slow as fuck. It also does more calculations that it needs, ##################
##################as it will calculate the same coefficient ranges multiple times ####################################
"""
import numpy as np
import itertools
import multiprocessing as mp

import time #to see how long it takes
start_time = time.time()
print("10:51")


#se calcularán todas las raíces de grado 1 a grado maxDg con coeficientes desde [-1,1]
#hasta [-maxCoef,maxCoef]
maxDg = 14
maxCoef = 1

processes = []

#generamos y solucionamos los polinomios
def generateAndSolve(grado, valorCoef):
    rangoCoef = [x for x in range(-valorCoef,valorCoef+1)]

    #creamos una lista que tenga todas las combinaciones posibles de longitud grado y posibles valores rangoCoef
    #la longitud es 1 menos de la adecuada, pero se añade luego
    #lo hacemos así para que no ponga 0 en la posición inicial, y además, reduce drásticamente la longitud de la lista
    coeficientes = list(itertools.product(rangoCoef, repeat=grado))

    roots = set()

    #iteramos por todos los valores en rangoCoef ignorando el 0. estos valores (i) serán el coeficiente del primer elemento
    #por eso no pueden ser 0. generamos y solucionamos los polinomios y añadimos las raíces a roots. 
    #por último devolvemos el set con las raíces. Usamos un set para evitar la presencia de duplicados
    rangoCoef.remove(0)
    for i in rangoCoef:
        for comb in coeficientes:
            p = np.poly1d([i]+list(comb))
            for n in p.r:
                roots.add(n)
    return roots

#añadimos al dicionario un nuevo valor con llave g(grado) con las raíces que surgen
#al ejecutar la generación de polinomios con ese grado y coeficientes
def addDegree(finalDict,dg,coef):
    finalDict["g%s"%(dg)] = generateAndSolve(dg,coef)
    print("subprocess %s has ended in %s seconds"%(dg, time.time()-start_time))

def main():
    global finalDict #me he visto forzado, si no daba error

    #para cada rango de coeficientes generamos una serie de procesos 
    #que ejecuten la función addDegree con todos los grados entre 1 y el máximo
    #estos procesos se ejecutarán al mismo tiempo para maximizar el processing power del ordenador 
    #y minimizar el tiempo que tarda en ejecutarse el programa.
    for coef in range(1,maxCoef+1):
        for dg in range(1,maxDg+1):
            processes.append(mp.Process(target=addDegree, args=(finalDict,dg,coef)))

        for p in processes:
            p.start()

        #esperamos a que termine el último proceso (el más largo, pues tiene el mayor grado), 
        #y decspués reseteamos la lista de procesos para que no de problemas en el siguiente loop 
        processes[-1].join()
        processes.clear()

        #cambiamos el tipo del finalDict a el de un diccionario normal de python
        #en vez de uno de manager.dict(), y creamos una lista inversa con los
        #valores entre el grado máximo y 1.
        finalDict = dict(finalDict)
        dgRange = [x for x in range(maxDg,0,-1)]

        #dado que las raíces de grado 5 contienen las de grado 4, podemos liberar espacio
        #quitando las raíces que coinciden. para conseguirlo, a cada grupo de raíces le quitamos el grupo inmediatamente inferior
        #por último, los valores presentes en el diccionario son raíces completas, lo cual no nos sirve,
        #por lo que las pasamos a una lista de listas donde las sublistas contienen los valores real e imaginario de cada raíz
        #guardamos el diccionario en un archivo cuyo nombre indique que valores contiene, limpiamos el diccionario para
        #liberar espacio y volvemos a pasar finalDict a un diccionario de tipo manager.dict()
        for i in dgRange:
            if i != 1:
                finalDict["g%s"%(i)] -= finalDict["g%s"%(i-1)]
            #finalDict["g%s"%(i)] = [[np.real(x) for x in finalDict["g%s"%(i)]],[np.imag(x) for x in finalDict["g%s"%(i)]]]
        print("------- %s seconds -------"%(time.time()-start_time))
        np.save("./Roots/Coeficientes_%s"%(coef),finalDict)
        finalDict.clear()
        finalDict = manager.dict()

#creamos un objeto multiprocessing.Manager() para poder crear un diccionario que los distintos procesos sean capaces de editar,
#llamamos main(), y cuando acabe el proceso printeamos el tiempo transcurrido.
if __name__ == "__main__": #comprobación necesaria por multiprocessing
    manager = mp.Manager()
    finalDict = manager.dict()
    try:
        main()
    except:
        print("FAILED")
        print("------- %s seconds -------"%(time.time()-start_time))

    print("------- %s seconds -------"%(time.time()-start_time))"""