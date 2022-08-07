
# for 반복문
lst = [1,2,3,4,5,10]
for i in lst:
    print(i)

for no in range(1,11):
    print(no)

#  1~100 중 5의배수 출력하기
for i in range(1,101):
    if i % 5 == 0 :
        print(i)

# while 구문 : 나무찍은 횟수 1씩 증가
treeHit = 0
while treeHit < 10 :
    treeHit += 1
    print("찍은횟수",treeHit)
    if treeHit == 10 :
        print("미션완료")

# for문으로 변경 (미션완료해도 100번까지 반복함, 단 break 구문 넣으면 멈춤=while 과 동일하게됨)

treeHit = 0
for i in range(1,101):
    treeHit += 1
    print("찍은횟수:", treeHit)
    if treeHit == 10 :
        print("미션완료")
        break

# rang (시작값, 끝값+1 , 증가값)
#  시퀀스변수 대신 _ 언더바 사용가능
for _ in range(1,101,3):
    print(_)

for _ in range(101,1,-3):
    print(_)

#  반복문으로 합계 구하기
#  1~100 사이의 수 중의 5의 배수 합계 구하기

hap = 0
for _ in range(1,101):
    if _ % 5 == 0 :
       hap += _ # hap = hap + 1 -> 합은 +1씩이라는 뜻이라서 위에 먼저 hap = 0이라고 변수선언해야함
    print('hap=%d' %(hap))

# 1~100 수 중 짝수, 홀수의 합계구하기
evenSum = 0 # 짝수의 합
oddSum = 0 # 홀수의 합

for _ in range(1,101):
    if _ % 2 == 0 :
        evenSum += _

    else:
        oddSum += _

print('짝수의 합: %d , 홀수의 합 : %d' % (evenSum, oddSum))



# 구구단 단 찍기
dan = int(input("확인 할려는 구구단 단을 입력하세요>>>"))
for _ in range(1,10):
    print("%d x %d = %d" % (dan,i,dan*i))

# 외부,내부 반복문 (구구단)
for dan in range(2,10): #2단부터 10단까지 의 외부반복문
    for i in range(1, 10): # 1부터 10까지 곱하는 내부반복문
        print("%d x %d = %d" % (dan, i, dan * i), end="\t")


# 두개의 주사위의 두눈의 합이 6이 되는 모든 경우의 수를 출력하시오
for i in range(1,7):
    for j in range(1,7):
        if i+j == 6:
            print("( %d , %d )" %(i,j))

# 1~100의 합계를 구하되, 3의 배수 제외하고 더하기 (컨티뉴사용)
hap, i = 0, 0

for i in range(1,101):
    if i % 3 == 0:
        continue
    hap += i
        print(i)

# 1. 비밀번호 확인
# 0987를 패스워드 #0987일때만 허용 그렇지 않을경우는 비허용 하 어려웡 ㅠㅠ

s_pwd = '@1234'

while True:
    i_pwd = ( input("비밀번호를 입력하세요>>>") )

    if i_pwd == s_pwd :
        print("환영합니다.")
        break
    else :
        print("잘못된 비밀번호 입니다.")
        continue

# 로또추출하기
import random










