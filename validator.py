import requests
from bs4 import BeautifulSoup

requests.urllib3.disable_warnings()

def code_validator():
    query = input('Code: ')
    url = 'https://jav.guru/?s={}'.format(query)

    proxy = {
        'http':'http://201.91.82.155:3128',
        'https':'https://201.91.82.155:3128'
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
        else:
            print('Code Not Found')
    else:
        print('Code Not Found')

def genre_validator():
    query = input('genre: ')
    url = 'https://jav.guru/?tag={}'.format(query)

    proxy = {
        'http':'http://201.91.82.155:3128',
        'https':'https://201.91.82.155:3128'
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
    else:
        print('Genre Not Found')

if __name__ == '__main__':
    print('''
    1. Code Validator
    2. Get link from genre
    ''')
    choice = input('No: ')
    if choice == '1':
        code_validator()
    elif choice == '2':
        genre_validator()
    else:
        print('Choice not found')