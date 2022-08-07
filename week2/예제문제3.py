

# 문제 2
while True :
    num = int(input("예상 숫자를 입력하세요. :"))
    com = random.randint(1,10)

    if num == com :
        print("~~성공~~")
        break
    elif num < com :
        print("더 작은 수 입력")
        continue
    else :
        print("더 큰 수 입력")
        continue


# 문제 3
total = 0
for i in range(1,101):
    if i % 2 == 0 and i % 3 != 0 :
        print(i , end=' ')
        total += i


# 2차원 리스트의 확장
# 파이썬빌라는 1호, 2호 라인이 있고 5층까지 존재합니다.
# 각층의 인구수와 빌라 전체의 거주 인구수를 구하시오.
del list
house = [ [2,3] , [5,2] , [2,6] , [4,7] , [1,4] ]
layer_total = 0
total = 0

for floor in range(0,5):
    print(house[floor])
    layer_total = 0
    for room in range(0,2):
        print('%d층의 %d호 거주 인구수 %d' %(floor+1 ,room, house[floor][room])
        total += house[floor][room]
        layer_total += house[floor][room]
        print('%d층의 거주 인구수 합계 %d' %(floor+1, layer_total))
print('파이썬빌라의 거주 인구수 합계 %d' %total))

# 튜플
tt1 = (10,20,30,40)
tt2 = ('A','B')
print(tt1+tt2)

# 단일 인수
t = 10 ; t1 = (10, )
t = (10)

# 여러개 인수
t2 = (1,2,3,4,5,3)
print(t2[0], t2[1:4], t2[-1])

#  튜플을 리스트형으로 형변환
mTT = (10,20,30)
mList = list(mTT)
print(mlist)
mList.append(40)
print(mList)
mTT = tuple(mList)




items = { "아메리카노":1500 , "라떼": 4500 , "밀크티":6500 , "레몬에이드":4500}
print(type(items))
print(items)
print(items["아메리카노"])
print(items.keys())
print(items.values())

# 원소수정
items["아메리카노"] = 2500
print(items)

#  삭제
del items["레몬에이드"]
print(items)

# 추가
items["유자차"] = 3000
print(items)

# 존재여부 검색
print( "유자차" in items)
print( "레몬에이드" in items)

for k in items.keys():
    print(k)

for k in items.values():
    print(k)

# get함수로도 value 값 가져옴
print(items.get("유자차"))
print(items["유자차"])

#dict 전체삭제
items.clear()



items = {"아메리카노": 1500, "라떼": 4500, "밀크티": 6500, "레몬에이드": 4500}
summary = 0;

while True :
    print("메뉴 : {0}". format(items))
    print("주문 종료시 5를 입력해주세요")
    a = input("어떤 음료를 드시겠습니까?")
    if a in items :
        summary += items[a]
        print("주문하신 메뉴는 {0} [{1}]원 입니다. 총 합계금액 {2}".format(a, items[a], summary))
    else :
        if a == "5":
            print("주문하신 총 합계금액 {0}".format(summary))
            break
        else:
            print("없는 메뉴 입니다.")
            continue

