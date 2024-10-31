import requests
import re

url = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
i = url.rfind("/")
print(i)
print(url[0:i])
print(url[0:i+1])
url = url[0:i+2] + "page_2.html"
print(url)

