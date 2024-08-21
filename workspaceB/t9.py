import requests
from bs4 import BeautifulSoup
import csv

name = "자바스크립트"
url = f"https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Used&SearchWord={name}"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
result_list = soup.select(".ss_book_list")
print(len(result_list))
books_info=[]
for result in result_list:
    book=[result.select_one("b").text,result.select_one("a")["href"]]
    books_info.append(book)
print(books_info)
with open("books77.csv",mode="w",newline="\n",encoding='utf-8') as f:
    writer=csv.writer(f)
    writer.writerows(books_info)
    #for row in books_info:
     #   writer.writerow(row)