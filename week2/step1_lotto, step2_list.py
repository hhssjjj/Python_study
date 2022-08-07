
import random

# print(random.random()*45)
print(random.randrange(1,46))
print(random.randrange(1,46))
print(random.randrange(1,46))
print(random.randrange(1,46))


import random
lotto_no = [] # 로또번호 저장리스트
lotto_ctn =0 # 로또번호 추출 횟수

while True:
    # 번호 추출
    lotto = random.randrange(1,46)
    # 중복 여부
    if lotto in lotto_no:
        lotto = random.randrange(1, 46)
        continue
    else:
        lotto_no.append(lotto)
        lotto_ctn += 1
        print("{}번째 로또 추출번호는 :{}".format(lotto_ctn,lotto))


    if lotto_ctn == 6:
        break

print(lotto_no)
a = [1,2,3,4,5]
b = []
for num in a :
    print(num , end="\t")
    b.append(num*3)

print(b)

# 리스트 내에 반복문 포함하기
a = [1,2,3,4,5,6,7]
b = [num*3 for num in a]
print(b)


a = [1,2,3,4,5,6,7]
b = []
for num in a :
    #print(num , end="\t")
    if num %2 == 0:
        b.append(num)
print(b)

# 리스트 내에 반복문,조건문 포함하기
a = [1,2,3,4,5,6,7]
b = [num for num in  a if num %2 == 0]
print(b)

# 1~100 사이의 수 중에 2의 배수와 5의 배수를 리스트에 담기 => 축약형
list = [ i for i in range(1,101) if i %2 ==0 or i %5 ==0]
print(list)


# 몇 번 반복하시겠습니까? >? 10
cnt = int(input("반복 횟수를 입력하세요"))
star = "*"
for i in range(0,cnt,1):
    print("%{}s".format(cnt)%star)
    star += "*"

list = ["키위","바나나","사과"]
print(list)
list.append("수박")  # 마지막에 들어감
print(list)
list.insert(2,"복숭아")
print(list)
list.remove("바나나")
print(list)

del list[0]
print(list)
list.pop()
print(list)
print(list.index("사과"))  #=> 찾는밸류(사과)가 첫번째 인덱스에 있다는 뜻


# 랜덤
string = "아이유 강호동 유재석 하하 비 BTS 악뮤"
member_list = []
for i in string.split():
    member_list.append(i)

print('올해의 MVP.{} '.format(member_list))
choice_member = random.choices(member_list, k=2)
print('올해의 MVP.{} '.format(choice_member))
mvp_member = random.choice(choice_member)
print('올해의 MVP는.{}'.format(mvp_member))

# 단일 list 예
a = [1,2,3,4,5]
print(a)
print(type(a))

for i in a :
    print(a[0:i])

'''
[1,2,3,4,5]
[2,3,4,5]
[3,4,2,]
[4,5]
[5] 
'''
a = [1,2,3,4,5]
for in a :
    print(a[i-1][:])

# 중첩리스트 객체 생성



# 2차원 리스트 만들기
list1= []
list2= []
value = 0
for i in range(0,4):
    for j in range(0,5):
        list1.append(value)
        value += 3
    list2.append(list1)
    list1=[] #초기화

print(list2)

# print(list2)
for i in range(0,4):
    for j in range(0,5):
        print("%3d"% list2[i][j] , end=" ")
    print("")


