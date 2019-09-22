## parser.py
import requests
from bs4 import BeautifulSoup
import json
import os

## python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://beomi.github.io/beomi.github.io_old/')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(
    'h3 > a'
    )

# ## my_titles는 list 객체
# for title in my_titles:
#     ## Tag안의 텍스트
#     print(title.text)
#     ## Tag의 속성을 가져오기(ex: href속성)
#     print(title.get('href'))

data = {}

for title in my_titles:
    data[title.text] = title.get('href')

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)

