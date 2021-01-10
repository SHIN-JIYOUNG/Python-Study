# <문자열 처리>

jumin="990120-1234567"

# 문자열 잘라내기 
print(jumin[7])
print(jumin[0:2])
print(jumin[:6])
print(jumin[7:])
print(jumin[-7:])
print("===============================")

python="python is Amazing"
print(python.lower())
print(python[0].isupper()) #boolean으로 반환
print(len(python))
print(python.replace("python", "java"))
index=python.index("n") #값이 없으면 오류 내고 끝내버림
print(index)
print(python.index("n", index+1))
print(python.find("n")) #값이 없으면 -1 반환
print(python.count("n"))

print("===============================")

print("나는 %d살 입니다" %20)
print("나는 %s를 좋아해요" %"파이썬")
print("Apple은 %c로 시작함" %"A")
print("나는 %s살 입니다" %20) # %s도 가능
print("나는 %s, %s색을 좋아합니다" %("파란", "빨간"))

print("나는 {}살 입니다".format(20))
print("나는 {}, {}색을 좋아합니다" .format("파란", "빨간"))
print("나는 {1}, {0}색을 좋아합니다" .format("파란", "빨간"))

print("나는 {age}살이고, {color}색을 좋아함". format(age=20, color="빨간"))

age=20
color="빨간"
print(f"나는 {age}살이고, {color}색을 좋아함")

print("===============================")

print("첫째줄\n둘째줄")
print("파이썬은 \"매력\"있다")

print("Red Apple\rPine") # 첫 문자열을 대신할 문자열로 바꿔줌
print("Redd \b Apple") # backspace
print("red\tapple")

print("===============================")

# 예제 풀이
url="http://naver.com"
url_ex=url.replace("http://","")
url_ex=url_ex[:url_ex.index(".")]
first=url_ex[:3]
mid=str(len(url_ex))
last=str(url_ex.count("e"))
password=first+mid+last
print(password)

print("===============================")

# 리스트(배열) 만들기 
numList=[10,20,30]
print(numList)

subway=["유재석", "조세호", "박명수"]
print(subway.index("조세호"))
subway.append("하하")
print(subway)
subway.insert(1, "정형돈")
print(subway)

# 맨 위부터 값 꺼내기
subway.pop()
print(subway)
subway.append("유재석")
subway.count("유재석")
print(subway)

numList=[5,2,4,3,1]
numList.sort() # 정렬
print(numList)
numList.reverse() # 순서 뒤바꾸기
print(numList)
# numList.clear() # 전체 삭제
# print(numList)

# 자료형 혼합 가능
mixList=["조세호", 10, True]
print(mixList)
# 리스트 합치기
numList.extend(mixList)
print(numList)

# tip: 프린트 사용법 
print("""
줄바꿈도
반영해줌
========================
""")
