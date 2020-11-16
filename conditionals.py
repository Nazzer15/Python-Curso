## Se comparan 2 valores iguales usando ==


x = 20

if (x > 30):
    print("x is less than 30")
else:
    print("x is greater than 30")



color = "black"
if color == "red":
    print("The color is red")
elif color == "blue":
    print("The color is blue")
else:
    print("Any color")


name = "John"
lastname = "Carter"

if name == "John":
    if lastname == "Carter":
        print("Hi my name is", name, lastname)
    else:
        print("You are not",name, lastname)   
else: 
    print("You are not", name, lastname)

y = 50

# Operadores logicos
if x > 2 and x <= 10:
    print("x is greater than two and less than ro rqueal to ten")
if x > 2 or x <= 20:
    print("x is greater than two or less than twenty")
if (not(x == y)):
    print("x is not equal y")    


