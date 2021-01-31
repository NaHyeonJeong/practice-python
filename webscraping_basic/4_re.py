import re # regular expression 정규식

############################################################
# 작성 순서
	# 1. p = re.compile("원하는 형태")
	# 2-1. m = p.match("careless") # match : 주어진 문자열의 '처음부터' 일치하는지 확인
	# 2-2. m = p.search("good care") # search : 주어진 '문자열 중에 일치하는게 있는지' 확인
	# 2-3. lst = p.findall("care cafe") # findall : 일치하는 모든 것을 '리스트 형태'로 반환
# 원하는 형태 : 정규식을 의미
	# . : 하나의 문자를 의미 ca.e - cafe
	# ^ : 문자열의 시작을 의미 ^de - desk
	# $ : 문자열의 끝을 의미 se$ - case
############################################################

# . : 하나의 문자를 의미 ca.e - cafe
# ^ : 문자열의 시작을 의미 ^de - desk
# $ : 문자열의 끝을 의미 se$ - case
p = re.compile("ca.e")

def print_match(m):
	if m:
		print("m.group() : ", m.group()) # 일치하는 문자열 반환
		print("m.string() : ", m.string) # 일치하는 문자열
		print("m.start() : ", m.start()) # 일치하는 문자열의 시작 index
		print("m.end() : ", m.end()) # 일치하는 문자열의 끝 index
		print("m.span() : ", m.span()) # 일치하는 문자열의 시작과 끝 index
	else:
		print("매칭되지 않음")

# m = p.match("careless") # match : 주어진 문자열의 '처음부터' 일치하는지 확인
# print_match(m)

# m = p.search("good care") # search : 주어진 '문자열 중에 일치하는게 있는지' 확인
# print_match(m)

lst = p.findall("care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)