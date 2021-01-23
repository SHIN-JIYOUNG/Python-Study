# <IO>

import sys
print("Python", "Java", file=sys.stdout) # sep: 값들의 사이를 ,로 채워줌 / end: 문장의 끝부분에 넣을 문자열 / #stdout 표준 출력
print("Python", "Java", file=sys.stderr) # 표준 에러

scores={"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(4), str(score).rjust(4), sep=(":")) # ljust, rjust(): 왼/오른쪽 정렬

# 은행 대기순번표
for num in range(1,21):
    print("대기번호: "+str(num).zfill(3)) # zfill: 빈 공간만큼 0 채워주기

# input값 대입
answer=input("아무 값이나 입력하세요: ") # input: 사용자가 값을 입력하고 엔터를 치면 answer에 그 값이 들어감
print(answer,"를 입력하였습니다.")


# <다양한 출력 포맷>

# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 빈 자리는 빈 공간으로 놔두고, >오른쪽방향으로 정렬을 하되 10자리 공간을 비운다

# 양수일 때는 +로 표시, 음수일 때는 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬, 빈칸은 _로 채움
print("{0:_<+10}".format(500))
# 3자리마다 콤마 찍어주기
print("{0:,}".format(10000000000))
# 3자리마다 콤마 찍어주기, +,- 부호 붙여주기
print("{0:+,}".format(10000000000))
print("{0:+,}".format(-10000000000))
# 3자리마다 콤마, 부호, 자리수 확보, 빈 자리는 ^로 채우기
print("{0:^<+30,}".format(10000000000))