import requests 
from bs4 import BeautifulSoup

keyword = 'python'
url = f'https://justjoin.it/?keyword={keyword}'

response = requests.get(url) 

html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

url_list = [] 
title = soup.find('title').get_text()
links = soup.find_all('a')

for link in links: 
    url = link.get('href')
    url_list.append(url)
    

# for url in url_list:
#     print(url)




# for i in range(len(url_list)):
for i in range(10):
    offer = url_list[i+1]
    url = f'https://justjoin.it{offer}'

    response = requests.get(url) 

    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    tech = soup.find_all('h6', class_='MuiTypography-root MuiTypography-subtitle2 css-x1xnx3')

    for t in tech:
        print(t.text)
    print(f'===== {i} ========================================')

