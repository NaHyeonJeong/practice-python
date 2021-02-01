# 다음 영화 1-5위 이미지 가져오고 저장하기
import requests
from bs4 import BeautifulSoup

for year in range(2015, 2020): # 2015 ~ 2019까지의 영화
	url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
	res = requests.get(url)
	res.raise_for_status()
	soup = BeautifulSoup(res.text, "lxml") # lxml이라는 파서를 통해 BeautifulSoup 객체를 만듬, soup이 모든 정보를 가지고 있음

	images = soup.find_all("img", attrs={"class":"thumb_img"})
	for idx, image in enumerate(images): # enumerate() : 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 때 사용, 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환
		# print(image["src"])
		image_url = image["src"] # img의 url을 가져옴
		if image_url.startswith("//"): # https: 가 없는 경우가 있음 - 넣어줘야 함
			image_url = "https:" + image_url
		print(image_url)
		# 가져온 정보를 파일로 저장
		image_res = requests.get(image_url)
		image_res.raise_for_status()

		with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
			f.write(image_res.content) # image_res가 가지고 있는 정보를 content로 쓴다

		if idx >= 4: # 상위 5위 까지의 이미지만 다운로드
			break