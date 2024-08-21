import requests
from bs4 import BeautifulSoup

name = "자바스크립트"
url = f"https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Used&SearchWord={name}"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
result_list = soup.select(".ss_book_list")

for result in result_list:
    book_name = result.select_one("b").text.strip()
    book_url = result.select_one("a")['href']
     # Modify this line to extract the href attribute
    print(f"Book Name: {book_name}")
    print(f"Book URL: http://www.aladin.co.kr{book_url}")
    print("----")