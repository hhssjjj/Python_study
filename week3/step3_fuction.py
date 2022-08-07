def add(a,b):
    return a+b

def minus(a,b):
    if a>b :
        return a-b
    else:
        return b-a

def multi(a,b):
    return a*b

def divide(a,b):
    if a>b:
        return a/b
    else:
        return  b/a

print(add(3,6))
print(minus(3,6))
print(multi(3,6))
print(divide(3,6))

while True:

    a = int(input('연산할 첫번째 수를 입력하세요'))
    b = int(input('연산할 두번째 수를 입력하세요'))
    oper = input('진행할 연산자를 입력하세요 +,-,*,/')

    if oper == '+':
        print('%d %c %d' %a,b,add(a,b))
    elif oper == '-':
        print('%d %c %d' %a,b,minus(a,b))
    elif oper == '*':
        print('%d %c %d' %a,b,multi(a,b))
    elif oper == '/':
        print('%d %c %d' %a,b,divide(a,b))
    else:
        break # -> while문 쓸 때는 들여쓰기해서 조건문을 포함시키고 else 써서 꼭 빠져나와야함.

# 아래 subject를 전역변수라고 부름
subject = { 'python':100 , 'Java':90 , 'HTML':88 }
# 아래 getSubPoint는 지역변수라고 부름
def getSubPoint():
    tot = 0
    sub = input('확인할 과목을 입력하세요')
    if sub in subject:
        print(subject[sub])
    else:
        print('확인할 과목이 존재하지 않습니다.')

getSubPoint()


