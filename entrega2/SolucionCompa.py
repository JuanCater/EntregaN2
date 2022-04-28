import csv
import os

def devolver_primera (archivo,lista):
  reader = csv.reader(archivo, delimiter = ',')
  header, datos = next(reader), list(reader)
  for elem in datos:
    if elem[11] == "1":
      if elem[6] == elem[7]:
        lista.append(elem[1])
    else:
      break
  return lista


path_arch = os.path.join(os.getcwd())
archivo_poke = "Pokemon.csv"

archivo= open(os.path.join(path_arch,archivo_poke),"r")
lista = []
devolver_primera(archivo,lista)
print(lista)


"""
data_poke = csv.reader(archivo, delimiter= ",")
header, datos = next (data_poke), list(data_poke)

print(datos)
"""