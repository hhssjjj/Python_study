# if문


import datetime

money = 2500

if money >= 3000 :
    print("욜 택시 타자")
else:
    print("걍 걸어가자")

# 입력 숫자의 홀,짝 구분하기 (비교연산자 ==, !=)
num1 = int(input("숫자를 입력하세요"))

if num1 % 2 == 0 :
    print("짝수입니다.")
else:
    print("홀수입니다.")

# 날짜
import datetime
today = datetime.datetime.now()
print(today)

day = today.weekday()
print(day)

# 0~4 평일 , 5 토, 6 일
if day >= 5 :
    print("주말")
else:
    print("평일")

# 다중 if문
score = 100
grade =""

if score >=90 :
    grade = "A"
elif score >= 80 :
    grade = "B"
elif score >= 70 :
    grade = "C"
elif score >= 60 :
    grade = "D"
else :
    grade = "F"

print(grade)

if score >=60 :
    grade = "합격"
else :
    grade = "불합격"

# 삼항연산자 (if구문 축약형)
grade = "합격" if score >= 60 else "불합격"
print(grade)

# if구문과 논리연산자 사용
eng = 70 ; math = 50

if eng >= 70 and math >= 80 :
    print("합격")
else :
    print("불합격")


# 계절 구분하기
import datetime
today = datetime.datetime.now()
month = today.month

# 3~5 : 봄, 6~8 : 여름, 9~11 : 가을, 12~2 : 겨울
if 3 <= month <= 5 :
    print("봄")
elif 6 <= month <= 8 :
    print("여름")
elif 9 <= month <= 11 :
    print("가을")
else:
    print("겨울")

# 중첩 if문
sex = '남'
age = 28

# 남자이면서 아동(~8) 초등학생(8~13), 중학생(14~16), 고등학생(17~19), 성인

if sex == '남':
    if age < 9:
        print("남자 아동입니다.")
    elif age < 14:
        print("남자 초등학생입니다.")
    elif age < 18:
        print("남자 고등학생입니다.")
    elif age < 20:
        print("남자 성인입니다.")
else :
    if age < 8:
        print("여자 아동입니다.")


