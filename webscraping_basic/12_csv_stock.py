# 코스피 시가 총액 순위
import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") # newline="" : 쓸데없는 줄바꿈 없애기 위함
writer = csv.writer(f) # csv 파일로 작성

# 각 열이 무엇에 대한 값인지를 알려주기 위함
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t") # split("\t") : [N, 종목명, 현재가, ....] 리스트 형태로 만들어줌
print(type(title))
writer.writerow(title) # writerow() : csv 파일로 행을 작성함, list 형태를 인수로 받음

for page in range(1, 5): # 1 부터 5 이전까지
	res = requests.get(url + str(page))
	res.raise_for_status() # 문제 있는지 확인 위함
	soup = BeautifulSoup(res.text, "lxml")

	# tbody의 tr에 있는 내용만 가져옴 (hhead에도 tr은 있지만 필요한 정보는 tbody에 있기 때문)
	data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
	for row in data_rows:
		columns = row.find_all("td") # tbody의 모든 tr에 있는 모든 td를 가져옴
		if len(columns) <= 1: # 의미 없는 tr의 공백은 td가 1개 이거나 없는 경우임 - skip
			continue
		# td의 내용을 텍스트로 찍음
		data = [column.get_text().strip() for column in columns] # strip() : 불필요한 개행, 탭 등을 없앰
		# print(data)
		writer.writerow(data) # csv 파일로 작성 : list 형태의 값을 인수로 줘야 함