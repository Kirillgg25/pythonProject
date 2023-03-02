import requests
from bs4 import BeautifulSoup
res_parse_list = []
response = requests.get("https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B5%D1%80%D0%BA%D0%B8")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("tr",{"class":"temperature"})
    res = soup_list[0].find("td")
print(res.text)