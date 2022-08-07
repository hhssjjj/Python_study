'''
import random

def letsgame():
word_list = ['가', '나', '다', '라', '마']

print(word_choice)
my_choice = input()
print(my_choice)
if word_choice == my_choice:
    print('통과입니다')
else:
    print('다시 입력하세요')
'''

'''
import random
word_list2 = ['안', '녕', '하', '세', '요']

i = 0
while i < 5:
    i += 1
    choice_word = random.choice(word_list2)
    print(choice_word)
    a = input()
    if a == choice_word:
        print('통과')

    else:
        print('다시 입력하세요')
'''


import random

w = ["고양이", "강아지", "말", "소", "양", "사자", "물개"]
print("타자게임 준비되면 엔터")
input()

q = random.choice(w)
n = 1
while n < 5:

    print("*문제", n)
    print(q)
    my_ans = input()
    if my_ans == q:
        print("통과")
        n += 1
        q = random.choice(w) #다음단어 제시
    else:
        print("다시")

