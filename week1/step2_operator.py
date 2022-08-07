
n1 = 10
n2 = 20

result = False
# == 같은지 비교
result = n1 == n2
print(result)

# != 서로 다른지 비교
result = n1 != n2
print(result)

# (2) 크기비교
result = n1 > n2
print(result)
result = n1 >= n2
print(result)
result = n1 < n2
print(result)
result = n1 <= n2
print(result)

# 논리연산자 and
result = n1 >= 10 and n2 <= 10
print(result)

# 논리연산자 or
result = n1 >= 10 or n2 <= 10
print(result)

# 논리연산자 not
result = not(n1 >=10)
print(result)

# 대입연산자= , (a,b) , 패킹할당(=대입)
v1 , v2 , v3 = 10,20,30
print(v1)
print(v2)
print(v3)

# 변수 교체
v2 , v1 = v1 , v2
print(v1)
print(v2)

# 패킹할당
lst = [1,2,3,4,5]
v1 , *v2 = lst
print(v1)
print(v2)
*v1 , v2 = lst
print(v1)
print(v2)
*v1, v2 , v3 = lst
print(v1)
print(v2)
print(v3)
*v1 , v2 = lst
print(v1)
print(v2)

# 복합연산자
x = 1000
print("초깃값 x=", x)
x +=2;
print("x += 2 후의 x=", x)
x +=2;
print("x -+ 2 후의 x=", x)
x +=2;

# 치환 (i=5이고 j는 i와 같다했을때 i를 바꾸더라도 j는 5)
i = 5
print(id(i))
j = i
print(id(j))

i = 10
print(j)

# input 은 문자함수라서 띄어쓰기에 영향받음
number1 = input("숫자를 입력하세요 >>>")
number2 = input("숫자를 입력하세요 >>>")
print(number1 > number2)

# 정수인 int를 처음number부터 넣어주거나 아니면 print에 넣어도 동일한 값 도출
number1 = input("숫자를 입력하세요 >>>")
number2 = input("숫자를 입력하세요 >>>")
print( int(number1) > int(number2))

number1 = int(input("숫자를 입력하세요 >>>"))
number2 = int(input("숫자를 입력하세요 >>>"))
print( (number1) > (number2))

# 예제문제
number1 = input("분자를 입력하시오 >>>")
number2 = input("분모를 입력하시오 >>>")
print( int(number1) // int(number2))
print( int(number1) % int(number2))

# 도움말 : print(내장함수)
print("010","4568","4567",sep="-")
print("하이" , end=", ")
print("하이")
print("하이")
print("하이")
print("하이")
print("하이")


str1 = "파이썬 기능 짱"
print(str1[2])

print(str1 + str1 + str1)
print(str1*4)

# len() -> length 길이, 즉 몇글자인지 뜻하는 내장함수
print(len(str1))

# type() -> datatype 알아보기 즉 인풋으로 들어온 함수가 정수인지 실수인지 등 뭔지 알 수 있음)
print( type(str1))

# format 내장함수
print( format(3.14159, '8.3f'))


print( format(12345, '10d'))
print( format(12345, '3,d'))

# 선언 3번째 방법
num1 = 10 ; num2 = 20
tot = num1 + num2
print(num1 + "+" + num2 + "=" + num1+num2)
# print(num1 , "+" , num2 , "=" , num1+num2)
print("10+20=%d" %tot)
print("%d+%d=%d" %(num1,num2,num,tot))
print('이름은 %s 이고, 나이는 %d 입니다.' %('홍길동' , 35))

# {}외부상수 적용도 가능
print('이름은 {1} 이고, 나이는 {0} 입니다.' .format('홍길동' , 35))

# 문자열 슬라이싱
str2 = "너무 좋습니다"
print(str2[3:5])







