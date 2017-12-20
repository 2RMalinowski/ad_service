from bs4 import BeautifulSoup
import requests

# first visit the login page to generate one

s = requests.session()

s.get('https://www.olx.pl/konto/?ref%5B0%5D%5Baction%5D=myaccount&ref%5B0%5D%5Bmethod%5D=index')

# now post to that login page with some valid credentials and the token
# from confing import zmienne
auth = {
    'login[email]': 't411701@mvrht.net'
    , 'login[password]': 'cobin4hood4'
}
s.post('https://www.olx.pl/konto/?ref%5B0%5D%5Baction%5D=myaccount&ref%5B0%5D%5Bmethod%5D=index', data=auth)


# now we should be authenticated, try visiting a protected page
# response = s.get('https://www.olx.pl/konto/?ref%5B0%5D%5Baction%5D=myaccount&ref%5B0%5D%5Bmethod%5D=index')
# print(response.text)


source_code = s.get('https://www.olx.pl/mojolx/odpowiedzi')
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")

# print(soup.find_all('div', {"class": "color-1 fnormal desc brkword"}))

for i in soup.find_all('div', {"class": "color-1 fnormal desc brkword"}):
    print(i.string)
