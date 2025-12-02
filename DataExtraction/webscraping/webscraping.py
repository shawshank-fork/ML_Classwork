import requests
from bs4 import BeautifulSoup

url = "https://www.geeksforgeeks.org/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')

    articles_titles = [tag.get_text(strip=True) for tag in soup.select("h2, h3")]
    print("\n article from GFG:\n")
    for t in articles_titles[:10]:
        print("-", t)


else:
    print("failed to retrive",response.status_code)

