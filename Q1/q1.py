import requests 
from bs4 import BeautifulSoup
import datetime

# target url
url = 'https://indianexpress.com/'

# making requests instance
reqs = requests.get(url)

# using the BeautifulSoup module
soup = BeautifulSoup(reqs.text, 'html.parser')
soup = soup.body
# displaying the title & url
data =[]
for news in soup.find_all('a', href=True):
    if len(news["href"]) > len(url) and len(news.get_text())>2:
        data.append({"Title": news.get_text(), "URL": news["href"]})
print(data)

