a = int(input("Introduce un entero (negativo para finalizar): "))
lista = []
while a >= 0 and a is not None:
    lista.append(a)
    a = int(input("Introduce un entero (negativo para finalizar): "))
i = 0
j = 0
if len(lista) > 0:
    for i in range(len(lista)):
        for j in range(len(lista)):
            if i != j and lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    for num in lista:
        print(num, end="\n")
else:
    print("La lista está vacía")