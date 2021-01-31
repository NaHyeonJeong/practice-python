import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # lxml이라는 파서를 통해 BeautifulSoup 객체를 만듬, soup이 모든 정보를 가지고 있음
# print(soup.title) # title태그 전체 내용을 가져옴
# print(soup.title.get_text()) # title태그의 내용만 가져옴
# print(soup.a) # soup 객체에서 처음 발견되는 a element를 반환
# print(soup.a.attrs) # attrs : 속성 정보를 사전 형태로 출력
# print(soup.a["href"]) # a element의 href 속성값 출력

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # 처음 발견되는 a태그의 element를 가져옴
# print(soup.find(attrs={"class":"Nbtn_upload"})) # 값이 하나 밖에 없는 경우에는 가능

# print(soup.find("li", attrs={"class":"rank02"}))
# rank1 = soup.find("li", attrs={"class":"rank01"})

# # 형제 노드로 이동하는 방법
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# print(rank1.next_sibling.next_sibling) # 줄바꿈 때문에 2번 사용함
# rank2 = rank1.next_sibling.next_sibling
# print(rank2.a.get_text())
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

# # 부모 노드로 이동하는 방법
# print(rank1.parent)

# # 다음/이전 노드를 쉽게 찾는 방법
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank1 = rank2.find_previous_sibling("li")
# print(rank1.a.get_text())

# # text 값으로 가져오는 방법
# webtoon = soup.find("a", text="독립일기-61화 동네 친구")
# print(webtoon)
