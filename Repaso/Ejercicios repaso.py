a = int(input("Introduce a: "))
b = int(input("Introduce b: "))
print(f"La suma de {a} y {b} es {a + b}")

print("====================================================")

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

print("====================================================")

dic = {'Pepe': 20, 'Manuel': 18, 'Ernesto': 21}
nombre = input("Introduce un nombre para conocer la edad: ")
if nombre in dic:
    print(dic[nombre])
else:
    print("No sé su edad")
