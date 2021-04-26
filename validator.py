import requests
from bs4 import BeautifulSoup

proxies = []

def get_proxy():
    res = requests.get('https://free-proxy-list.net/', headers={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(res.text,"lxml")
    for items in soup.select("#proxylisttable tbody tr"):
        proxy_list = ':'.join([item.text for item in items.select("td")[:2]])
        proxies.append(proxy_list)

requests.urllib3.disable_warnings()

def code_validator(pr, query):
    url = 'https://jav.guru/?s={}'.format(query)
    try:
        proxy = {
            'http':'http://'+pr,
            'https':'https://'+pr
        }
        req = requests.get(url, timeout=10, proxies=proxy, verify=False).text
        soup = BeautifulSoup(req, 'html.parser')
        div = soup.find('div', class_='inside-article')
        if div:
            a_link = div.findAll('a', href=True)
            p = div.find('p', class_='tags')
            if p:
                a_tags = p.findAll('a')
                title_genre = ' '.join([str(elem.text) for elem in a_tags])
                print('Link: ' + a_link[0]['href'])
                print('Genre: ' + title_genre)
                return True
            else:
                print('Code Not Found')
                return True
        else:
            print('Code Not Found')
            return True
    except Exception as e:
        return False

def genre_validator(pr, query):
    try:
        url = 'https://jav.guru/tag/{}'.format(query)
        proxy = {
            'http':'http://'+pr,
            'https':'https://'+pr
        }
        req = requests.get(url, timeout=10, proxies=proxy, verify=False).text
        soup = BeautifulSoup(req, 'html.parser')
        row = soup.findAll('div', class_='row')
        if row:
            for card in row:
                grid = card.find('div', class_='grid1')
                h2 = grid.find('h2')
                a_link = h2.find('a', href=True)
                print('Title: ' + a_link.text)
                open('link.txt','a').write(a_link['href']+'\n')

            print('\n\n Saved as link.txt')
            return True
        else:
            print('Genre Not Found')
            return True
    except Exception as e:
        return False

if __name__ == '__main__':
    print('''
    1. Code Validator
    2. Get link from genre
    ''')
    choice = input('No: ')
    if choice == '1':
        query = input('Code: ')
        get_proxy()
        for i in proxies:
            if code_validator(i, query) == True:
                break
            else:
                pass
    elif choice == '2':
        query = input('genre: ')
        get_proxy()
        for i in proxies:
            if genre_validator(i, query) == True:
                break
            else:
                print('Wait Rotate Proxy')
                pass
    else:
        print('Choice not found')
