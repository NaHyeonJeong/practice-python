import requests
from bs4 import BeautifulSoup

url = "https://sonyunara.com/shop/search.php?searchOrder=&keyword=150"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # lxml이라는 파서를 통해 BeautifulSoup 객체를 만듬, soup이 모든 정보를 가지고 있음

# imgs = soup.find_all("a", attrs={"class":"image"})
# for img in imgs:
# 	print(img.img["src"])

# infos = soup.find_all("div", attrs={"class":"info"}) # find_all : list 형태로 반환
# for info in infos:
# 	txt = info.find("div").get_text()
# 	print(txt)

print()
print(">>> 150을 위한 옷 검색 결과 <<<")
print()
itemContents = soup.find_all("div", attrs={"class":"item-content"})
for itemContent in itemContents:
	pullLeft = itemContent.find("div", attrs={"class":"pull-left"}).get_text()
	subject = itemContent.find("div", attrs={"class":"subject"}).get_text()
	link = "https://sonyunara.com/" + itemContent.find("div", attrs={"class":"subject"}).a["href"]
	print(pullLeft, end='')
	print(subject, link)