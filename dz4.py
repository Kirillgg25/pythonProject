brands_of_car = ["BMW", "Lada", "Volvo"]
print(brands_of_car)
a = input(f"Я хочу собі авто марки ")
def auto():
    if a in brands_of_car:
        print(f"{a} марка авто зі списку {brands_of_car.index(a)+1}!")
    else:
        print("Такого авто немае вибиреть з списка")
        print(brands_of_car)
c = auto()


brands_of_car.append("Ferrari")
del brands_of_car[2]
print(brands_of_car)
