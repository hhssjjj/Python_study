# P.217
'''
텍스트 파일 입출력(file input/output)
-데이터 입출력 시(file. db) 반드시 예외 처리한다.
형식) open('파일경로/파일명, mode = 'r' or 'w' or 'a')
'''


# open(file=, mode=,
help(open)

#현재 시스템의 정보를 가져오는 모듈
import os
print(os.getcwd()) #절대경로

# alt + shift + e : 영역실행
# C:\wonGit

# alt + shift + f10 : 파일실행
# C:\wonGit\week6


def ex1():
    # f = open('week6/food_e.txt', 'r')
    f = open('food_e.txt', 'r')
    content = f.read()
    print(content)
    print(type(content))
    # apple\nbababa\n

# 한줄 읽어오기
def ex2():
    # f = open('week6/food_e.txt', 'r')
    # line_data = f.readline()
    # print(line_data) #한줄 읽어오기
    # print(type(line_data))
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())

    f = open('week6/food_e.txt', 'r')
    for i in range(10):
        # line_data = f.readline().replace("\n","") #이스케이프 문자 \n 제거방법1
        line_data = f.readline().strip() #이스케이프 문자 \n 제거방법1
        if line_data == 'pear':
            print('배 찾음', line_data)
        else:
            print('배 없음', line_data)


# 한글파일 읽어오기
def ex3():
    #상대경로 영역실행
    f = open('week6/food_k.txt', 'r', encoding="utf8")
    # read() 파일 전체를 읽어옴
    content = f.read()
    print(content)
    print(type(content))

# 파일 쓰기
def ex4():

    try:
        str = "고양이 사자 강아지 호랑이 얼룩말 코끼리 나무늘보" #짤라서 리스트에 넣어보기
        w_list = str.split(' ')
        print(w_list)

        f = open('week6/animal.txt', 'w', encoding="utf8")
        for w in w_list:
            f.write(w+' ')
        f.close()
    except Exception as e:
        print('예외발생:', e)
    # 마지막에 파일 닫기 꼭 할 수 있도록 finally를 지정함.
    finally:
        f.close()


# 파일 이어 쓰기

def ex4():

    try:
        str = "고양이 사자 강아지 호랑이 얼룩말 코끼리 나무늘보" #짤라서 리스트에 넣어보기
        w_list = str.split(' ')
        print(w_list)

        f = open('week6/animal.txt', 'a', encoding="utf8")
        for w in w_list:
            f.write(w+'\n')
        f.close()
    except Exception as e:
        print('예외발생:', e)
    # 마지막에 파일 닫기 꼭 할 수 있도록 finally를 지정함.
    finally:
        f.close()

# 파일열기 with 사용하여 열기
def ex5():
    with open('week6/food_k.txt', 'r', encoding="utf8") as f :
        #여러줄을 한번에 읽어오기 리스트로 변환됨
        content_list = f.readlines()
        print(type(content_list))
        print('문단수:', len(content_list))

def ex6():
        with open('week6/food_k.txt', 'r', encoding="utf8") as f:
        contents = f.read()
        print(type(content_list)) # type은 string
        print('글자수:', len(contents))