'''
1. 함수(Function)
-특정 1개 기능을 정의
- 내장함수. 사용자 정의 함수
1. 내장함수 : built-in or import
   - built-in : 함수()
   - import :  모듈.함수()
2. 사용자 정의 함수
형식)
def 함수([인수])
     실행문
     실행문
     [:return 값']
'''
# 1. 함수
dataset = list(range(1,6))
print(dataset) #[1,2,3,4,5]

# (1) built-in 함수
print('len=', len(dataset))
print('sum=', sum(dataset))
print('max=', max(dataset))
print('min=', min(dataset))

# (2) import 함수
import statistics #수학/통계 함수 모듈 방법1

print('평균=', statistics.mean(dataset)) #방법2
print('중위수=', statistics.median(dataset))

from statistics import variance, stdev #방법2 (내가 만드는 function을 쓰겠다.)
print("표본 분산=", variance(dataset))
print("표본 표준편차=", stdev(dataset))

# 방법3 from statistics import *  -> (전부다 끌고 오겠다, 소스가 거대해짐, 불필요한것 까지 모두)

# 2. 사용자 정의 함수

#(1) 인수가 없는 함수
def userFunc1():
    print('인수가 없는 함수')
    print('userFunc1')

userFunc1() # 함수호출

# (2) 인수가 있는 함수
def userFunc2(x, y):
    print('userFucn2')
    z = x + y
    print('z=', z)

userFunc2(10, 20)

# (2) return 있는 함수
def userFunc3(x, y) :
    print('userFunc3')
    tot = x + y
    sub = x - y
    mul = x * y
    div = x / y

    return tot, sub, mul, div
#실인수 :  키보드 입력
x = int(input('x입력 : '))
y = int(input('y입력 : '))

t, s, m, d = userFunc3(x, y)
print('tot =', t)
print('sub =', s)
print('mul =', m)
print('div =', d)



# (2) 각 숫자에 8을 더해라
a = [10,20,30,40]


def plusList(a):
    print(a)
    new_list = []
    for no in a:
        new_list.append(no+8)

    return new_list

plus_list = plusList(a)

print(plus_list)


'''
함수의 가변인수
- 한 개 가인수로 여러 개 실인수 받을 수 있는 인수
형식) def 함수명(*인수)
'''
def Func1(name, grade, *subject) :
    print(name)
    print(grade)
    print(subject) #가인수는 튜플 () 로 불러와서 변경되지않는 인수

Func1("아이유", "1학년", "재즈", "발라드", "팝", "트로트")

from statistics import mean, variance, stdev

def statics( type , *data):
    if type == 'avg':
        return mean(data)
    elif type == 'var':
        return variance(data)
    elif type == 'std':
        return stdev(data)
    else:
        return "type err"

print('avg=' , static('avg' , 1,2,3,4,5,6))  # 튜플로 가인수
print('var=' , static('var' , 1,2,3,4,5,6))
print('std=' , static('std' , 1,2,3,4,5,6))

#(3) 사전형 가변인수 **두개 씀
def emp_fucn(name, age, **other):
    print(name)
    print(age)
    print(other) # {'addre : '서울시', 'height' : 175, 'weight': 65}

emp_fucn('홍길동', 35, addre='서울시', height=175, weight=65 , phone='01012345678')

# 동전 앞뒷면
import random

def coin(n):
    result = []
    for i in range(n):
        r = random.randint(0,1)
        if ( r == 1):
            result.append(1) #앞면
        else:
            result.append(0) #뒷면

    return result

# print(coin(10))


def montaCoin(n):
    coin_set = coin(15)
    print('합계:', sum(coin_set))
    print('통계:', sum(coin_set)/n) #던진 횟수만큼 나눔
    return sum(coin_set)/n

print(montaCoin(30))
print(montaCoin(300))
print(montaCoin(3000))
print(montaCoin(30000))

'''
2. 축약함수
'''


#(1) 일반함수
def Adder(x, y):
    add = x + y
    return  add

print('add = ', Adder(10,20))

# 축약형
print('add = ', (lambda x , y : x+y )(10,20) ) # add = 30
print('add = ', (lambda x , y : x*y )(10,20) ) # add = 200

# 몸체는 pass 하고 나중에 코딩 가능
def divide(x,y):
    pass

#디폴트 값 정하지 않음
def sayhello(name , msg):
    print("안녕",name + ',' + msg)

sayhello('한솔', '반가워!')  # 안녕 한솔,반가워

#디폴트 값 정함
def sayhello(name, msg='반갑습니당.'): # msg 는 디폴트함수가 된다.
    print("안녕", name + ',' + msg)


sayhello('한솔') # 안녕 한솔,반갑습니당.