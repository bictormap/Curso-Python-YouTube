n1 = input("Ingresa el primer numero: ")
n2 = input("Ingrese el segundo numero: ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
Para los numeros {n1} y {n2},
el resuldtado de la suma es {suma},
el resuldtado de la resta es {resta},
el resuldtado de la multiplicacion es {multi},
el resuldtado de la division es {div}.
"""

print(mensaje)
