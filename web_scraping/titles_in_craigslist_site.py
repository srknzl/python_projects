from bs4 import BeautifulSoup
import requests

url = "https://boston.craigslist.org/search/sya?query=macbook+pro+touchbar"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data,"html.parser")
titles =  soup.find_all("a",{"class":"result-title"})
for title in titles:
  print title.text.encode("utf-8")
