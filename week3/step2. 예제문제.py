
# 110p 1번
lst = [10, 1, 5, 2]

noList = lst*2
print(noList)

# 첫번째 인덱스 값에 *2 하기
noList.append(noList[0]*2)
print(noList)

# 홀수 인덱스 요소 값만 출력하기
seq =0
result2 = []
for i in noList :
    if seq % 2 != 0 :
        result2.append(i)
    seq += 1
print(result2)

# 2번 (a형)
a = int( input("생성할 숫자 개수를 입력하시오") )
import random

dataset = []
for i in range(5):
    r = random.randint(1,50)
    dataset.append(r)

print(dataset)

# 선생님 답안
in_list_size = int( input('생성할 숫자 개수를 입력하시오'))

random_list = []
for i in range(1, in_list_size+1):
    random_list.append(i*3)

print(random_list)

#축약형 vector_list = [ i*3 for i in range(1,in_list_size+1)
in_list_size = int( input('생성할 숫자 개수를 입력하시오'))
vector_list = [ i*3 for i in range(1,in_list_size+1) ]
print(vector_list)


#vector 데이터를 set 으로 형변환해서 중복 숫자 지우고 유니크한 숫자만 남기기
in_list_size = int( input('생성할 숫자 개수를 입력하시오'))
vector_list_set = set(vector_list)
print(vector_list_set)


import random

in_list_size = int( input('생성할 숫자 개수를 입력하시오'))
vector_list = [  random.randint(0,30) for i in range(1,in_list_size+1) ]
print(vector_list)
vector_list_set = set(vector_list)
print(vector_list_set)

while True :
    number = int( input("찾는 숫자를 입력하세요") )
    if (vector_list.count(number) > 0 ):
        print("{0}은 있습니다." .format(number))
        vector_list_set.remove(number)
        print(vector_list_set)
    else :
        print("{0}은 없습니다.".format(number))
        print(vector_list_set)
    if len(vector_list_set) ==0 :
        break
print("모든 숫자를 찾았습니다.")


# 3번
message = ['spam','ham','spam','ham']
trans_massage = []

for i in message:
    if i == 'spam':
        trans_massage.append(1)
    elif i == 'ham':
        trans_massage.append(0)
print(trans_massage)

# 축약형
message = ['spam','ham','spam','ham']
trans_massage2 = [ 1 if i =='spam' else 0 for i in message ]
print(trans_massage2)


# 4번
position = ['과장','부장','대리','사장','대리','과장']
uni_position = list(set(position))
print('중복되지 않는 직위 : ', uni_position)
position_cnt = {}
for i in position:
    if i in position_cnt:
        position_cnt[i] += 1
    else:
        position_cnt[i] = 1
print('각 직위별 빈도수: ', position_cnt)


