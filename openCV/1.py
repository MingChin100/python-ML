import csv
import codecs
import requests
import io
import json
from bs4 import BeautifulSoup
# # word=input("關鍵字:")
# r1=requests.get("https://ecshweb.pchome.com.tw/search/v3.3/?q=apple")

# # r=json.loads(r1.text)
# r1.encoding="utf8"
# print(r1.text)


r1=requests.get(
	"https://www.google.com/search?q=%E5%95%86%E6%A5%AD%E5%88%86%E6%9E%90%E8%88%87%E6%95%B8%E6%93%9A%E5%88%86%E6%9E%90%E7%9A%84%E5%B7%AE%E5%88%A5&rlz=1C1SQJL_zh-TWTW898TW898&oq=%E5%95%86%E6%A5%AD%E5%88%86%E6%9E%90%E8%88%87%E6%95%B8%E6%93%9A%E5%88%86%E6%9E%90%E7%9A%84%E5%B7%AE%E5%88%A5&aqs=chrome..69i57j0l4.10270j0j7&sourceid=chrome&ie=UTF-8")
r1.encoding="utf8"
print(r1.text)