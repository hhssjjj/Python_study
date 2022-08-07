
# {key : [var1, var2]} - {'영화' [평점, 관객수]}

movie = {'광해' : [9.24, 1200], '공작' : [7.86, 500], '관상' : [8.01, 900] }

for title in movie.items():
    print(title)

for title , info in movie.items():
    print(title , info )

# 문제1. 평점 8이상인 영화제목과 누적관객수 출력하기
# 평점 info[0]:평점, info[1]:누적관객수

tot = 0
for title , info in movie.items():
    print(len(info)) # 9.24는 len 1 이고 1200은 len2 이다.
    if info[0] >= 8.0 :
        print(title)
        tot += info[1]
print('누적 관객수 = ', format(tot, '3,d')) # 3,d 에서 3은 백의자리수에 콤마찍겠다!

foods = {"떡볶이":"오뎅" ,
         "짜장면":"단무지" ,
         "라면":"김치" ,
         "피자":"피클" ,
         "맥주":"땅콩" ,
         "치킨":"치킨무" ,
         "삼겹살":"상추" };


while True :
    myfood =  ( input(str(list(foods.keys())) + "중 좋아하는 음식은?") )
    if myfood in foods :
        print("<%s> 궁합 음식은 <%s>입니다." % (myfood, foods.get(myfood)))
        continue
    else :
        print("그런 음식이 없습니다.")
        break

#내가좋아하는 음식은?
while True :
    myfood =  ( input(str(list(foods.keys())) + "중 좋아하는 음식은?") )
    if myfood in foods :
        print("<%s> 궁합 음식은 <%s>입니다." % (myfood, foods.get(myfood)))
    elif myfood == "끝" :
        break
    else :
        print("그런 음식이 없습니다.")





# 단어 빈도수 구하기
charset = ['바나나', '사과', '딸기', '망고','딸기', '딸기', '딸기']
wc = {}

for key in charset:
    # 리스트이 값의 존재 여부에 따라서 해당갯수가 증가해야함
    if key in wc:
        wc[key] += 1
    else:
        wc[key] = 1
    #wc[key] = wc.get(key, 0) + 1    -> if 구문의 축약형
    print(key)
print(wc)

# [실습] 축약형을 사용하여 문자 빈도수 구하기[1]
charset = ['abc', 'code', 'band', 'band', 'abc']
wc ={}
for key in charset:
    wc[key] = wc.get(key, 0) + 1
    print(key)
print(wc)

# 최고 출현 단어
print('max =', max(wc, key=wc.get))


# 다른 메모리 주소로변경
a = 10
print(id(a))
a = 20
print(id(a))


# 2. 깊은 복사 : 내용복사 (내용동일 ,주소 다름)
import copy

name = ['홍길동', '이순신', '강감찬']
name2 = copy.deepcopy(name)
print(name)
print(name2)
print('name address =', id(name))
print('name address =', id(name2))

# 원본 수정
name[1] = "이순신장군"
print(name)
print(name2)


# 커피 주문하기 (주문 내역서 까지)
items = {"아메리카노": 1500, "라떼": 4500, "밀크티": 6500, "레몬에이드": 4500}
summary = 0;
wc = {}

while True :
    print("메뉴 : {0}". format(items))
    print("주문 종료시 5를 입력해주세요")
    a = input("어떤 음료를 드시겠습니까?")
    if a in items :
        summary += items[a]
        print("주문하신 메뉴는 {0} [{1}]원 입니다. 총 합계금액 {2}".format(a, items[a], summary))
        wc[a] = wc.get(a,0) + 1
    else :
        if a == "5":
            print("주문하신 총 합계금액 {0}".format(summary))
            break
        else:
            print("없는 메뉴 입니다.")
            continue

print("주문내역 : {0}".format(wc))


# 1~100사이의 랜덤수 10개 뽑기 randint
import random

dataset = []
for i in range(10):
    r = random.randint(1,100)
    dataset.append(r)

print(dataset)
#max = min = ~ 이용하여서 최대값과 최솟값 구하기

amax = amin = dataset[0]

for i in dataset:
    if amax < i:
        amax = i
    if amin > i:
        amax = i

print('amax = ', amax)
print('amin = ', amin)


# (1)오름차순 정렬방법

dataset = [3,5,1,2,4]
n = len(dataset)
o_seq = 0
for i in range(1,n+1) :
    print(dataset[o_seq]) #반복문을 돌게끔 선언을 해주어야함 오씨퀀스 = 0
    o_seq += 1

for i in range(0,n-1):
    # print(dataset[i]
    for j in range(i+1,n):
        if dataset[i] > dataset[j]:
            tmp = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] = tmp
    print(dataset)
print(dataset)


# 오름차순 정렬 두번째 방법
dataset = [3,5,1,2,4]
n = len(dataset)
for i in range(0,n-1) :
    print(dataset[i])   # -> 범위를 조정하면 반복문 시퀀스 따로 없이 가능


for i in range(0,n-1):
    # print(dataset[i]
    for j in range(i+1,n):
        if dataset[i] > dataset[j]:
            tmp = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] = tmp
    print(dataset)
print(dataset)

