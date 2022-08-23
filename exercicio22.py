lista_original = [90, 50, 10, 80, 10, 30, 40, 70, 20, 30, 60]

lista_modificada = []

for elemento in lista_original:
    if elemento not in lista_modificada:
        lista_modificada.append(elemento)

lista_ordenada = sorted(lista_modificada)
tupla = tuple(lista_ordenada)
print("A lista original eh: ", lista_original)
print("A tupla ficou assim :", tupla)