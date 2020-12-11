import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

# load url
page = urllib.request.urlopen('https://pythonprogramming.net/')
soup = bs(page , features = "html.parser")
print(soup)


names = soup.body.findAll('dt')

print(names)

# .\w+ means random. and any strings after 
function_names = re.findall('id="random.\w+')
