demo_list= [1, 'hello', 1.34, True, [1,2,23,4]]
colors = ['red', 'green', 'blue']

numbers_list = list((1,2,3,4,5))
# print(numbers_list)
# Crear una lista desde el numero 1 al 999
# r = list(range(1, 1000))
# print(r)

# Obtener metodos que puedo obtener de la lista
# print(dir(colors))

# print(colors[-2])

# print('green' in colors) # True

# print(colors)
# colors[1] = 'yellow'
# print(colors)
# El append solo puede pasar un elemento por parametros
# colors.append('violet')
# print(colors)

# Pero con el uso de una dupla o un array se pueden pasar varios elementos
# colors.append(['violet', 'black', 'white'])
print(colors)

# Pero los incluye con parentesis

# Extend permite añadir mas valores al array
# colors.extend(['violet', 'blue', 'black'])
# print(colors)

# Insert permite añadir valores en el indice deseado
colors.insert(1, 'purple')
# Insert en el final del array
colors.insert(len(colors), 'black')
print(colors)


# Remover elementos
# Remueve el ultimo del array
colors.pop()
colors.pop()
print(colors)

colors.remove('green')
print(colors)

# Elimino el indice que le pase
colors.pop(0)
print(colors)

# Limpio todos los elementos del array
colors.clear()
print(colors)


colors.extend(['Japon', 'Costa Rica', 'Corea'])
print(colors)

# Orden alfabetico
colors.sort()
print(colors)


# Orden alfabetico con reverse
colors.sort(reverse = True)
print(colors)


# Imprimir el indice del array
print(colors.index('Japon'))

# Cuenta los indices del array
print(colors.count('Corea'))
























