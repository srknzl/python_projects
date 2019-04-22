from bs4 import BeautifulSoup
import requests
import time

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print color.BOLD + "Printing the results of searching 'macbook pro touchbar' in boston.craigslist.org site" + color.END 
print "Waiting you to read for 5 seconds"
time.sleep(3)
url = "https://boston.craigslist.org/search/sya?query=macbook+pro+touchbar"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data,"html.parser")
results =  soup.find_all("li",{"class":"result-row"})
for result in results:
  title_tag = result.find("a",{"class": "result-title"})
  title = title_tag.text.encode("utf-8") if title_tag else "N/A"
  link_tag = result.find("a",{"class": "result-title"})
  link = link_tag.get("href").encode("utf-8") if link_tag else "N/A"
  date_tag = result.find("time",{"class":"result-date"})
  date = date_tag.text if date_tag.encode("utf-8") else "N/A"
  price_tag = result.find("span",{"class":"result-price"})
  price = price_tag.text  if price_tag.encode("utf-8") else "N/A"
  address_tag = result.find("span",{"class":["result-hood","nearby"]})
  address = address_tag.text.replace("(","").replace(")","").encode("utf-8") if address_tag else "N/A"


  print color.RED + color.BOLD + "Title:" + color.END + color.END + title
  print color.BLUE + color.BOLD + "Link:" + color.END + color.END + link
  print color.DARKCYAN + color.BOLD + "Date:" + color.END + color.END  + date
  print color.GREEN + color.BOLD + "Price:" + color.END + color.END  + price 
  print color.YELLOW + color.BOLD + "Address:" + color.END + color.END  + address
  print 
