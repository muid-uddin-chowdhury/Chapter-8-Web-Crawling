import requests
import re

url = "http://books.toscrape.com/index.html"
response = requests.get(url)
response.ok
text = response.text
text_len = len(text)
print(text_len)
result = re.findall(r'<div class="side_categories">(.*?)</div>', text, re.M | re.DOTALL)
result_len = len(result)
print(result_len)
print(type(result))
print(result)