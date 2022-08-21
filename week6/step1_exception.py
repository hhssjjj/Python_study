'''
예외처리
'''

# 오류 발생 코드
def ex1():
    x = [10, 20, 30, 'apple', 14, 51]

    print('프로그램 시작')
    for i in x:
        y = i**2
        print(y)

    print('프로그램 끝')

# 예외처리
def ex2():
    x = [10, 20, 30, 'apple', 14, 51]

    print('프로그램 시작')
    try:
        for i in x:
            y = i**2
            print(y)
    except:
        print('오류발생')

    print('프로그램 끝')


# 예외처리 2
def ex3():
    x = [10, 20, 30, 'apple', 14, 51]

    print('프로그램 시작')
    for i in x:
        try:
            y = i**2
            print(y)
        except:
            print('오류발생')

    print('프로그램 끝')

# 예외처리 3
def ex4():
    x = [10, 20, 30, 'apple', 14, 51]

    print('프로그램 시작')
    for i in x:
        try:
            y = i**2
            print(y)
        except TypeError:
            print('TypeError 오류발생 :  자료형확인')

    print('프로그램 끝')

# 예외처리 4
def ex5():
    x = [10, 20, 30, 'apple', 14, 51]

    print('프로그램 시작')
    for i in x:
        try:
            y = i**2
            print(y)
        except TypeError as e:
            print('TypeError 오류발생 :  자료형확인', e)

    print('프로그램 끝')


import builtins
print(dir(builtins))

# 예외처리 5
for i in range(10):
    try:
        print(10 / i)

def ex6():
    for i in range(10):
        try:
            print(10 / i)
        except ZeroDivisionError as e:
            print("Not divivded by 0")
            print(e)

def ex6_1():
    for i in range(10):
        try:
            print(10 / i)
        except ZeroDivisionError as e:
            print("Not divivded by 0")
            print(e)
        예외상황과 상관없이 무조건 실행
        finally:
            print('프로그램 종료')

def ex7():
    try:
        div = 1000 / 2.53
        print('div = %5.2f' % (div))
        #div = 1000 / 0 # 오류발생 1
        #f = open('c:\\a.txt') # 오류발생 2
        num = int(input('숫자입력 : ')) # 오류발생 3
        print('num =', num)
    except ZeroDivisionError as e:
        print('오류정보 1 :', e)
    except FileNotFoundError as e:
        print('오류정보 2 :', e)
    except Exception as e:
        print('오류정보 3 :', e)
    finally:
        print('모든 예외상황 확인')

# raise 예외 발생
# 미리 알아야 할 예외 정보가 조건에 만족하지 않을 경우, 예외를 발생시키는 구문이다.
while True:
    value = input('변환 할 정수 값을 입력해 주세요.') #문자열 string
    for digit in value:
        if digit not in "0123456789":
            raise ValueError("숫자값만 입력 가능")  #오류 없는데 일부러 오류를 만들어서 잘못 입력했다고 알려줌
    print('변환된 정수값:', int(value))