# 쿠팡에서 페이지 바꿔가면서 노트북 검색하기
import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}
for i in range(1, 6):
	# 페이지를 바꾸기 위해 format(i)을 사용
	print("페이지 : ", i)
	url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)

	res = requests.get(url, headers=headers)
	res.raise_for_status()
	soup = BeautifulSoup(res.text, "lxml") # lxml이라는 파서를 통해 BeautifulSoup 객체를 만듬, soup이 페이지의 모든 정보를 가지고 있음

	items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
	for item in items:
		# 광고 제품 제외 출력 
		ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
		if ad_badge:
			# print(" >>> 광고 상품 제외 <<< ")
			continue

		# Apple 제품 제외
		name = item.find("div", attrs={"class":"name"}).get_text() # 제품명
		if "Apple" in name:
			# print(" >>> Apple 상품 제외 <<< ")
			continue

		price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격
		
		rate = item.find("em", attrs={"class":"rating"}) # 평점 - 없는 경우 있음
		if rate:
			rate = rate.get_text()
		else:
			# print(" >>> 평점 없는 상품 제외 <<< ")
			continue
		rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) # 평점 수 - 없는 경우 있음
		if rate_cnt:
			rate_cnt = rate_cnt.get_text()[1:-1] # 예 : (26) - 괄호 없애야 카운트 체크 가능
		else:
			# print(" >>> 평점 수 없는 상품 제외 <<< ")
			continue

		link = item.find("a", attrs={"class":"search-product-link"})["href"]
		# 평점이 있고 평점 수도 있는 경우만 걸러진 상태에서
		# 평점이 4.5 이상이고 리뷰 100개 이상인 제품만 조회되도록 함
		if float(rate) >= 4.5 and int(rate_cnt) >= 100:
			print(f"제품명 : {name}")
			print(f"가격 : {price}")
			print(f"평점 : {rate}점({rate_cnt}개)")
			print("바로가기 : {}".format("https://www.coupang.com" + link))
			print("-"*100) # 줄 긋기