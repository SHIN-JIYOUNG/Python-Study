# <key>

cabinet = {3:"유재석", 100:"김태호"} #key:value 의 데이터가 들어가는 것.
print(cabinet[3]) #3번 열쇠에는 유재석이 들어있음
print(cabinet.get(5)) #값 없어서 none 반환 
print(cabinet.get(5,"사용 가능")) # none이 반환된다면 "사용 가능" print
# print(cabinet[5]) #.get 함수 안쓰면 프로그램 에러와 함께 종료

print(3 in cabinet) #true
print(5 in cabinet) #false

#정수가 아닌 String도 가능
cabinet={"A-3":"유재석"}
#값 추가
cabinet["C-20"]="조세호" #key와 값 추가, 만약 먼저 값이 있으면 값을 업데이트 해줌
print(cabinet)
#값 없애기
del cabinet["A-3"]
print(cabinet)
#key들만 출력
print(cabinet.keys())
#values들만 출력
print(cabinet.values())
#key+value 쌍
print(cabinet.items())
#값 모두 비우기
cabinet.clear()


# <tuple>
# 내용 변경 불가한 list가 튜플이다
menu =("돈까스", "치즈까스")
print(menu[0])
# menu.add("생선까스") # err
name="김종국"
age=20
hobby="코딩"
print(name, age, hobby)
(name, age, hobby)=("유재석", 30, "코딩2")
print(name, age, hobby)


# <set(집합)>
# 중복 안됨, 순서 없음
my_set={1,2,3,3,3}
print(my_set)
java={"유재석","김태호","양세형"}
python=set(["유재석","박명수"])
# java와 python의 교집합?
print(java & python)
print(java.intersection(python))
# 합집합?
print(java | python)
print(java.union(python))
# 차집합?
print(java-python)
print(java.difference(python))
# python(set)에 값 추가
python.add("김태호")
print(python)
# java에서 값 제거
java.remove("김태호")


# <자료구조의 변경>
menu={"커피","우유","주스"}
print(menu)
print(menu, type(menu))
menu=list(menu) #set을 list로 변경 
menu=tuple(menu) #tuple로 변경
menu=set(menu) #set으로 변경


# Quiz. 추첨을 통해 1명은 치킨, 3명은 커피쿠폰 증정.
# 댓글은 20명 작성, 아이디는 1~20, 중복당첨 불가, random의 shuffle과 sample 활용
from random import *
users=range(1,21) # 1부터 20까지 숫자 생성 (21 직전까지라는 뜻)
users=list(users)
print(users)
shuffle(users)
print(users)
winners=sample(users,4)# 무작위로 list에서 n개 뽑아낸다
print("치킨: {0}".format(winners[0]))
print("커피: {0}".format(winners[1:]))