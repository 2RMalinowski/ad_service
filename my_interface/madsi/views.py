from madsi.models import myAnswer
from bs4 import BeautifulSoup
import requests
from config import log_mail, log_pass


url = 'https://www.olx.pl/konto/?ref%5B0%5D%5Baction%5D=myaccount&ref%5B0%5D%5Bmethod%5D=index'
s = requests.session()
s.get(url)
auth = {
    'login[email]': log_mail
    , 'login[password]': log_pass
}
s.post(url, data=auth)

source_code = s.get('https://www.olx.pl/mojolx/odpowiedzi')
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")

for i in soup.find_all('div', {"class": "color-1 fnormal desc brkword"}):
    print(i.string)


def add_message(request):
    if requests.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['name']
            email = form.cleaned_data['text']
