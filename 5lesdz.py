from colorama import Fore, Back, Style # Наши модули

print(Fore.RED + "Hi") # Fore - цвет текста
print(Back.BLACK + "Hi") # Back - цвет фона
print(Style.DIM + "Hi") # DIM - делает цвет тусклее
print("Hi") # Как можем заметить настройки сохраняються так что нам ножно сбросить командой ниже
print(Style.RESET_ALL)
print("Hi")