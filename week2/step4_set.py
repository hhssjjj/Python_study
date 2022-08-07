
s = {1,3,5,3,1}
print(s)

for d in s :
    print(d, end=' ')
print()

s2 = {3,6}

print(s.union(s2)) # 합집합 : s + s2 = {1,3,5,6}
print(s.difference(s2)) # 합집합 : s + s2 = {1,3,5,6}
print(s.intersection(s2)) # 교집합 : {3}

s3 = {1, 3, 5}
print(s3)
s3.add(7) # 원소추가
print(s3)

s3.update([5, '다섯'])
print(s3)

sMenu = ["가","나","다","가","다"] #리스트 중복 허용
print(type(sMenu))
sMenu = set(sMenu)
print(type(sMenu))

lMenu = list(sMenu)
print(lMenu)

def sayhello():
    print('안녕하세요')
    print('저는 최원화입니다')

sayhello()
sayhello()
sayhello()










