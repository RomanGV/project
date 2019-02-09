import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.westernunion.ru/ru/ru/transliteration-table.html')
soup = BeautifulSoup(req.content, 'html.parser')
dic = []
# f= soup.find_all("section", class_="rmt-layout-row rmt-paddingBottom")
# t= soup.find_all("td")

t_list = [td.text.strip() for td in soup.find_all("td")]
t_list.append((' ', ' '))

# word = td_list[0].split('\n')
# print(t_list)
