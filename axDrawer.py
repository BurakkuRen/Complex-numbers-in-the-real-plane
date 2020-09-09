import matplotlib.pyplot as plt
import numpy as np

grado = 1
coeficiente = 1
soloCoeficiente = False

rows = 1
columns = 1

fig, ax = plt.subplots(rows, columns)

roots = np.load("./Roots/Values")

for i in list(range(1, grado+1)):
    value = roots["g%s"%(i)]["c%s"%(coeficiente)]
    if soloCoeficiente == False:
        for i in list(range(1, coeficiente)):
            value2 = roots["g%s"%(i)]["c%s"%(i)]
            value[0] += value2[0]
            value[1] +=value2[1]
            value2.clear()

    ax.plot(value[0],value[1], "o", markersize=1, label="g%s"%(str(i)))


plt.show()

