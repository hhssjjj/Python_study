import random
import time

def getStartWordGame(cnt):
    w = ["고양이", "강아지", "말", "소", "양", "사자", "물개"]
    print("타자게임 준비되면 엔터")
    input()

    start_t = time.time()
    print(start_t)
    q = random.choice(w)
    n = 1
    while n < cnt:

        print("*문제", n)
        print(q) #문제를 보여줍니다.
        my_ans = input()
        if my_ans == q:
            print("통과")
            n += 1
            q = random.choice(w)  # 다음단어 제시
        else:
            print("다시")

    end_t = time.time()
    d_time = end_t - start_t
    f_time = format(d_time, ".2f")

    print("총 소요시간:", f_time, "초")