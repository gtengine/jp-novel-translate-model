import requests
from bs4 import BeautifulSoup

res = requests.get("https://kakuyomu.jp/works/1177354054884195461")
print(res.status_code)