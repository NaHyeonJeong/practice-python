import requests

# res = requests.get("http://nadooding.tistory.com")
#########################################################
# 필수적인 묶음으로 생각하기
res = requests.get("http://google.com")
res.raise_for_status() # 올바르게 가져왔으면 아무 문제 없음, 문제 있으면 프로그램 종료
#########################################################
print("웹 스크래핑 진행")
print("응답코드 : ", res.status_code) # 200 : 정상 동작

# if res.status_code == requests.codes.ok:
# 	print("정상입니다")
# else:
# 	print("문제가 생김 [에러코드 ", res.status_code, " ]")

# 스크래핑 내용을 보여줌
# print(len(res.text))
# print(res.text)

# 스크래핑 한 내용을 파일처리
with open("mygoogle.html", "w", encoding="utf8") as f:
	f.write(res.text)