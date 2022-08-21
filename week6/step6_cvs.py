#import pandas as p
#import os

# def ex1():
#     score_csv = p.read_csv('meta-data/csv/score.csv')
#     print(score_csv.info())
#     print(score_csv.head())
#
#     kor = score_csv.kor # 객체의 컬럼명
#     eng = score_csv['eng']
#     mat = score_csv['mat']
#     dept = score_csv['dept']
#     print('kor max:', max(kor))
#     print('eng max:', max(eng))
#     print('mat max:', max(mat))
#
#     print('kor min:', min(kor))
#     print('eng min:', min(eng))
#     print('mat min:', min(mat))
#
#     from statistics import mean
#     print('kor mean:' , round(mean(kor),3))
#     print('eng mean:' , mean(eng))
#     print('mat mean:' , mean(mat))
#
#     #중복을 허용하지 않는 컬렉션 set 만들기
#     dept_cnt = {} #튜플
#     #key:value
#     for key in dept:
#         dept_cnt[key] = dept_cnt.get(key,0) + 1
#
#     print(dept_cnt) #시험 본 횟수
#
#     #{101: 5, 102:5, 103:5}

import pandas as p
import os

def ex2():
    score_csv = p.read_csv('meta-data/csv/bmi.csv')
    print(score_csv.info())
    print(score_csv.head())

    w = score_csv['weight']
    label = score_csv['label']

    print('최대몸무게', max(w))
    # 중복을 허용하지 않는 컬렉션 set 만들기
    label_cnt = {}  # 튜플
    # key:value
    for key in label:
        label_cnt[key] = label_cnt.get(key, 0) + 1

    print(label_cnt)

    # {101: 5, 102:5, 103:5}








