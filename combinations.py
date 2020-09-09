import itertools

grado = 0
coeficiente = 0

def products(grado,coeficiente):
  rangoCoef = [x for x in range(-coeficiente,coeficiente+1)]
  combinaciones = list(itertools.product(rangoCoef,repeat=grado+1)) 


#el algoritmo que las soluciona:
roots = []

for comb in coeficients:
    p = np.poly1d(comb)
    for n in p.r:
        roots.append(n)
OR

for comb in coeficients:
    p = np.poly1d(comb)
    roots += p.r
