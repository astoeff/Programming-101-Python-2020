import requests
from bs4 import BeautifulSoup
import re
import string

responce = requests.get('https://register.start.bg/')
responce.encoding = 'utf-8'
content = responce.content
soup = BeautifulSoup(content, 'html.parser')
links = soup.find_all('a')
count = 0
# reg = "href=\"http[" + ''.join(string.printable) + "]*'.'bg[" + ''.join(string.printable) + "]*\""
reg = "href=\"http[" + ''.join(string.printable) + "]*\.bg"
for link in links:
    if bool(re.search(reg, str(link))):
        print(link)
print(count)
