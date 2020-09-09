import itertools

grado = 0
coeficiente = 0

rangoCoef = [x for x in range(-coeficiente,coeficiente+1)]
combinaciones = list(itertools.product(rangoCoef,repeat=grado+1)) 
