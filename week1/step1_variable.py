a = 100
print(a)
print( id(a) )

a = 200
print(a)
print( id(a) )

# 한줄주석
# 여러줄 주석 """ ㄹㄹㄹ """
# 2진수 -> 10진수
b = bin(0)
print(b)
print( int(b,0))


# 2진수 -> 10진수 -> 8진수
f = bin(42)
print(f)
print( oct(int(f,2)))


# 2진수 -> 10진수 -> 16진수
g = bin(34)
print(g)
print(hex(int (g,2)))

# 변수 선언
# 실수형
var1 = 120.4
# 논리형
var2 = True
print(var2)
# 문자열
var3 = hi


# 산술연산
x = 7
y = 4
print("7+4", x+y)
print("7-4", x-y)
print("7*4", x*y)
print("7/4", x/y)
print("7%4", x%y)

# 복합연산자
num +=2  # -> 2씩 늘어남

# 자료형변환
# 1. int 실수 -> 정수
i = int(10.5)
j = int(20.42)
add = i+j
print(add)
print(10.5+20.42)

# 2. float 정수 -> 실수
o = 10
o = float(o)

# 문자열
str = '10'
print( int(str)**3)
