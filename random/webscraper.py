import requests
from bs4 import BeautifulSoup as bs

github_user = input("Enter Github username: ")
user = 'justkeating'
url = 'https://www.github.com/' + github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_img = soup.find('img')['src']
print(profile_img)