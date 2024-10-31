import requests
import re

url = "http://books.toscrape.com/index.html"
response = requests.get(url)
response.ok
text = response.text
text_len = len(text)
print(text_len)
catagory_pat = re.compile(r'<li>\s*<a href="(.*?)">(.*?)<', re.M | re.DOTALL)
result = re.findall(catagory_pat, text)
print(len(result))
print(result[0])
print(result[1])