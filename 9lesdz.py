import requests
res_parse_list = []
from bs4 import BeautifulSoup
response = requests.get("https://www.oschadbank.ua/currency-rate")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("td",{"class":"heading-block-currency-rate__table-col"})
    res = soup_list[10]
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("td", {"class": "heading-block-currency-rate__table-col"})
    res1 = soup_list[9]

a = int(input("Укажите что будете делать \n"
              "1 Долары в гривнах\n"
              "2 Гривны в доларах"))
b = float(res.text)
d = float(res1.text)
if a == 1:
    dol = int(input("Долар "))
    print(dol * d)
elif a == 2:
    uah = int(input("Гривны"))
    print(uah / b)