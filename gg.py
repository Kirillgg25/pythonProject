import turtle
a = int(input("Ведите число для размера триугольника и квадрата "))
for a in range(3):
    turtle.forward(a)
    turtle.left(50)
    print(a)

turtle.exitonclick()