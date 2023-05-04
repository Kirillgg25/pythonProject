a = []
x = input("Ведите число ")
while x != 'stop':
    a.append(int(x))
    x = input("Ведите число ")
print(max(a))
print(min(a))