import itertools
import numpy as np
import sqlite3

db = sqlite3.connect('combinations_1.db')
index = 0
c = db.cursor()
c.execute('''
  CREATE TABLE combinaciones (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    REAL FLOAT,
    IMAG FLAOT,
    GRADO INTEGER,
    COEF INTEGER
  )''')
db.commit()
grado = 10
coeficiente = 10

def products(grado,coeficiente):
  rangoCoef = [x for x in range(-coeficiente,coeficiente+1)]
  [Process(x) for x in itertools.product(rangoCoef,repeat=grado+1)]
  return "a"

def Process(product):
  global index
  p = np.poly1d(product)
  grado = len(product) - 1 - CountZeroes(product)
  coef = abs(max(product, key=abs))
  for n in p.r:
    InsertIntoDataBase(np.real(n), np.imag(n), grado, coef)
    index += 1

def CountZeroes(inputList):
  count = 0
  for i in inputList:
    if i != 0:
      return count
    count += 1
  
  return count

def InsertIntoDataBase(real, imag, grado, coef):
  global c, db
  c.execute("INSERT INTO combinaciones VALUES (NULL, ?, ?, ?, ?)", [real, imag, grado, coef])
  db.commit()

  print(index)

products(grado, coeficiente)
db.close()