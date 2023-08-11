import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://news.google.com/search?q=hdfc%20bank&hl=en-IN&gl=IN&ceid=IN%3Aen"

r = requests.get(url)
print(r)
r.html.render()

soup = BeautifulSoup(r.text, "lxml" )
print(soup.prettify)
