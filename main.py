import requests 
from bs4 import BeautifulSoup

keyword = 'python'
iterations = 10

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
stack = []
for i in range(iterations):
    if iterations+1 <= len(url_list):
        offer = url_list[i+1]
        url = f'https://justjoin.it{offer}'

        response = requests.get(url) 

        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        tech = soup.find_all('h6', class_='MuiTypography-root MuiTypography-subtitle2 css-x1xnx3')

        print(f'===== {i+1} ========================================')
        for t in tech:
            print(t.text)
            stack.append(t.text)

print('=======================================================')
stack.sort()
__import__('pprint').pprint(stack)

