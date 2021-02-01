from bs4 import BeautifulSoup as bs
import requests as req




headers={

    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'

         }
url='https://www.eldorado.ru/cat/detail/monitor-acer-r221qbmid-black/?show=response#customTabAnchor'

resp=req.get(url, headers=headers)
soup=bs(resp.text, 'lxml')
a=soup.find_all('div', class_='userReviewDate')
b=soup.find_all('div', class_='middleBlockItem')
c=soup.find_all('div', class_='userInfo')

for i in range(0, len(a)):
    q=c[i].text.strip()
    w=a[i].text.strip()
    e=b[i].text.strip()
    print(q, w, e)

