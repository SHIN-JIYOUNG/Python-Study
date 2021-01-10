# <if>
weather=input("오늘 날씨는 어때요?") # 사용자의 입력값 받기
if weather=="비" or "눈": # 조건
    print("우산을 챙기세요") # 실행
elif weather=="맑음":
    print("준비물이 필요없어요")
else:
    print("날씨를 다시 확인하세요")

temp=int(input("오늘 기온이 몇 도예요?"))
if 30<=temp:
    print("너무 더워요")
elif 10<=temp and temp<30:
    print("날씨가 좋아요")
elif 0<=temp and temp<10:
    print("조금 추워요")
else:
    print("너무 추워요, 나가지 마세요")


# <for>
for waiting_no in [0,1,2,3,4]:
    print("대기번호: {0}".format(waiting_no))
for waiting_no in range(5): # 0 1 2 3 4
    print("대기번호: {0}".format(waiting_no))
for waiting_no in range(1,6): # 1 2 3 4 5
    print("대기번호: {0}".format(waiting_no))

starbucks=["아이언맨", "토르", "아이엠그루트"]
for customer in starbucks:
    print("손님: {0}".format(customer))


# <while>
customer="토르"
index=5
while index>=1: #조건
    print("{0}의 커피는 {1}잔 남았습니다".format(customer, index))
    index-=1
    if index==0:
        print("주문하신 커피가 모두 나왔습니다")

#customer="아이언맨"
#while True: # 무한루프
#    print("{0}님의 커피가 나왔습니다".format(customer))

customer="토르"
person="Unknown"
while person!=customer:
    print("{0}님이시라면 커피를 가져가주세요".format(customer))
    person=input("이름을 입력해주세요.")


# <continue / break>
absent=[2,5] # 결석한 학생
no_book=[7] #책을 안가져온 학생
for student in range(1,11): #1~10번까지의 출석번호에서
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지, {0}는 교무실로 오세요.".format(student))
        break
    print("{0}번 학생, 책 읽어주세요.".format(student))


# 한 줄로 끝내는 for문 
# 출석번호가 1 2 3 4로 가는데 앞에 100을 더하기로함

students=[1,2,3,4,5]
print(students)
student=[i+100 for i in students]
print(student)

# 학생들 이름을 길이로 변환
students=["Iron man", "Thor", "I am groot"]
students=[i.upper() for i in students]
print(students)
students=[len(i) for i in students]
print(students)


# 문제.
# 나는 택시 기사이다. 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구해보자.
# 조건) 승객별 운행 소요 시간은 5~50분 사이 난수로 정해짐, 나는 5~15분 사이 승객만 매칭 가능
from random import *
cnt=0 #총 탑승 승객 수
for i in range (1,51): # 1~50명의 승객
    time=randrange(5,51) # 5~50분 사이의 소요 시간
    if 5<=time <=15: # 5~15분 이내 손님, 매칭 성공
        print("[O] {0}번째 손님 (소요시간 {1}분)".format(i, time))
        cnt+=1
    else: # 매칭 실패
        print("[ ] {0}번째 손님 (소요시간 {1}분)".format(i, time))
print("총 탑승승객", cnt,"명")
