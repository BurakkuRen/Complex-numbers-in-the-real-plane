import itertools
import numpy as np
import sqlite3

db = sqlite3.connect('combinations_10000.db')
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

pending = []

def products(grado,coeficiente):
  rangoCoef = [x for x in range(-coeficiente,coeficiente+1)]
  [Process(x) for x in itertools.product(rangoCoef,repeat=grado+1)]
  return "a"

def Process(product):
  global index, pending
  p = np.poly1d(product)
  grado = len(product) - 1 - CountZeroes(product)
  coef = abs(max(product, key=abs))
  for n in p.r:
    pending.append((np.real(n), np.imag(n), grado, coef))
    if (index % 10000 == 0):
      InsertIntoDataBase(pending)
      pending = []
    index += 1

def CountZeroes(inputList):
  count = 0
  for i in inputList:
    if i != 0:
      return count
    count += 1
  
  return count

def InsertIntoDataBase(inList):
  global c, db
  c.executemany("INSERT INTO combinaciones VALUES (NULL, ?, ?, ?, ?)", inList)
  db.commit()

  print(index)

products(grado, coeficiente)
db.close()