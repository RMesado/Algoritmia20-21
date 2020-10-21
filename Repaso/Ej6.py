from math import sqrt


def ecuacion(a, b, c):
    if (b ** 2) - (4 * a * c) < 0:
        return None
    else:
        sol1 = (-b + sqrt((b ** 2) - (4 * a * c))) / (2 * a)
        sol2 = (-b - sqrt((b ** 2) - (4 * a * c))) / (2 * a)

        return sol1, sol2


a = int(input("Introduce el valor de a: "))
b = int(input("Introduce el valor de b: "))
c = int(input("Introduce el valor de c: "))

if ecuacion(a, b, c) is None:
    print("No hay solución real")
else:
    sol1, sol2 = ecuacion(a, b, c)
    if sol1 == sol2:
        print(f"La solución es {sol1}")
    else:
        print(f"Las soluciones son {sol1} y {sol2}")
