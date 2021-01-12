# <function>
def open_account(): #함수 선언- def 함수명 ():
    print("새로운 계좌가 생성되었습니다")

open_account() # 함수 호출

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance+money))
    return balance + money

def withdraw(balance, money):
    if balance>=money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance-money))
    else:
        print("출금하려는 금액이 잔액보다 큽니다. 잔액은 {0}원 입니다.".format(balance))
    return balance

def withdraw_night(balance, money):
    commission =100 #수수료 100원
    return commission, balance-money-commission
balance = 0 # 계좌의 돈
balance = deposit(balance, 1000)
balance = withdraw(balance,500)
commission, balance=withdraw_night(balance, 500)
print("수수료는 {0}원이며 잔액은 {1}원 입니다.".format(commission, balance))

def profile(name, age, main_lang):
    print("이름: {0}, 나이: {1}, 주 사용 언어: {2}".format(name,age,main_lang))
profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업이라면?-> 기본값을 만들어주기
def profile(name, age=17, main_lang="파이썬"): # 전달된 값이 없다면 기본값을 반환하는 것
    print("이름: {0}, 나이: {1}, 주 사용 언어: {2}".format(name,age,main_lang))
profile("유재석")
profile("김태호")

# 키워드를 이용하여 호출해보기
def profile(name, age, main_lang):
    print(name, age, main_lang)
profile(name="유재석", main_lang="파이썬", age=20)


# <가변인자>를 이용한 함수 호출
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름: {0}, 나이: {1}".format(name, age), end=" ") # 프린트가 끝나면 " " 공백만 주고 밑의 문장 계속 출력 가능 
    print(lang1, lang2, lang3, lang4, lang5)
profile("유재석", 20, "python","Java","C","C++","C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "") # 이러한 상황 (값이 적어져야하거나, 늘어나야 하는 경우)에서 가변인자가 필요

def profile(name, age, *language):
    print("이름: {0}, 나이: {1}".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()
profile("유재석", 20, "python","Java","C","C++","C#", "Javascript")
profile("김태호", 25, "Kotlin")


# <지역변수, 전역변수>
gun=10

def checkpoint(soldiers): # 경계근무
    global gun #전역변수를 사용하겠다는 키워드는 global
    gun=gun-soldiers
    print("[함수 내에서] 남은 총: {0}개".format(gun))
print("전체 총: {0}개".format(gun))
checkpoint(2) 
print("남은 총: {0}개".format(gun))

def checkpoint_ret(gun, soldiers):
    gun=gun-soldiers
    print("[함수 내에서] 남은 총: {0}개".format(gun))
    return gun

print("전체 총: {0}개".format(gun))
gun=checkpoint_ret(gun,2)
print("남은 총: {0}개".format(gun))


# <퀴즈> 표준 체중을 구하는 프로그램 작성
# 표준체중: 각 개인의 키에 적당한 체중, 남: 키(m)*키*22, 여: 키*키*21
# 조건: 표준체중은 별도의 함수 내에서 계산 (함수명: std_weight / 전달값: 키(height), 성별(gender)), 표준체중은 소수점 둘째자리까지 표시

def std_weight(height, gender):
    if gender=="남자":
        return height*height*22
    else :
        return height*height*21
height=175
gender="남자"
weight=round(std_weight(height/100,gender), 2)
print("키 {0}cm {1}의 표준체중은 {2}kg 입니다.".format(height,gender,weight))