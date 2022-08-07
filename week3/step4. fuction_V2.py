# 2022.07.17
# 작성자: ~~~
# 용도: ~~~


import random
import math

# 함수선언
def getNumber():
    return random.randrange(1,46)

lotto_no = []

print('로또번호 추첨 시작 ')
while True:
    num = getNumber()
    if lotto_no.count(num)  == 0:
        lotto_no.append(num)

    if len(lotto_no) >= 6:
        break

print('추첨된 로또 번호는 ==>')
print(lotto_no)


