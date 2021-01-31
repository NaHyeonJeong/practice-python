import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=335885"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # lxml이라는 파서를 통해 BeautifulSoup 객체를 만듬, soup이 모든 정보를 가지고 있음

# # 만화 제목 + 링크 가져오기
# cartoons = soup.find_all("td", attrs={"class":"title"})
# for cartoon in cartoons:
# 	title = cartoon.a.get_text()
# 	link = "https://comic.naver.com" + cartoon.a["href"]
# 	print(title, link)

# 평점 구하기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
	rate = cartoon.find("strong").get_text()
	print(rate)
	total_rates += float(rate)
print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates / len(cartoons))