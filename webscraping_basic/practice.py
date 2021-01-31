import requests
from bs4 import BeautifulSoup

url = "https://sonyunara.com/shop/search.php?searchOrder=&keyword=150"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # lxml이라는 파서를 통해 BeautifulSoup 객체를 만듬, soup이 모든 정보를 가지고 있음

imgs = soup.find_all("a", attrs={"class":"image"})
for img in imgs:
	print(img.img["src"])


infos = soup.find_all("div", attrs={"class":"subject"}) # find_all : list 형태로 반환
for info in infos:
	print(info.get_text())
