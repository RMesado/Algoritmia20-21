dic = {'Pepe': 20, 'Manuel': 18, 'Ernesto': 21}
nombre = input("Introduce un nombre para conocer la edad: ")
if nombre in dic:
    print(dic[nombre])
else:
    print("No sé su edad")
