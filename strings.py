myStr = "HellO WoRld!!"

# print(dir(myStr))
# Upper case
print(myStr.upper())
# Lower case
print(myStr.lower())
# Swap case upper to lower
print(myStr.swapcase())
# Capitalize pone mayuscula la inicial de la cadena de caracteres
print(myStr.capitalize())
# Raplace la primera palabra es la reemplazada
print(myStr.replace('HellO', 'Hola').upper())
# Count cada caracter en la cadena
print(myStr.count('l'))
print(myStr.count(' '))
# StartsWith empieza con la palabra entre los parentesis
print(myStr.startswith('Hello')) # False
print(myStr.startswith('HellO')) # True
# EndsWith termina con la palabra entre los parentesis
print(myStr.endswith("World")) # False
print(myStr.endswith("!"))     # True
# Split separa las palabras en un array
print(myStr.split())
# Find busca la letra en la cadena del string y devuelve el numero de su posicion
print(myStr.find("o"))
print(myStr.find("k")) #-1 cuando no se encuentra
# len cantidad de caracteres
print(len(myStr))
# index muestra la ubicacion de los caracteres
print(myStr.index('W'))
# isalpha - isnumeric, es un numero?
print(myStr.isalpha)
print(myStr.isnumeric)
# Imprimir solo un caracter
print(myStr[4])
# Imprimir caracter inverso
print(myStr[-1])

print("Hola mundo" + myStr)
print("Hola mundo" , myStr)
# f busca la variable para poder imprimirla
print(f"Hola mundooo {myStr}")



