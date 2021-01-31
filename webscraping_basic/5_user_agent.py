import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

# 스크래핑 한 내용을 파일처리
with open("nadocoding.html", "w", encoding="utf8") as f:
	f.write(res.text)