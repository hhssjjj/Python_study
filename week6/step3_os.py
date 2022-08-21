# import os
# print(os.getcwd()) # 현재 경로 확인
#
# print(os.chdir('')) # 디렉토리 이동
#
# print(os.listdir('.')) # 현재 디렉토리 목록 확인
#
#
# #디렉토리 생성
# os.mkdir('meta-data')
# #디렉토리 삭제
# os.rmdir('meta-date')
# #다중 디렉토리 생성
# os.makedirs('meta-data/log')
# #다중 디렉토리 삭제
# os.removedirs('meta-data/log')
#
# #windows 파일 경로를 조작하는 모듈
# import os.path
# print(os.getcwd())
#
# #절대경로
# os.path.abspath('food_e.txt')
# #포함 디렉토리 확인
# os.path.dirname('week6/step1_exception.py')
# #디렉토리 존재여부
# os.path.exists('C:\wonGit\week6')
# #파일 존재여부 확인
# os.path.isfile('C:\wonGit\week6\step2_txt_file.py')
# #파일 사이즈 확인
# os.path.getsize('C:\wonGit\week6\step3_os.py')

# def makeLofFile():
#log 디렉토리의 존재여부 확인
#week6 log 디렉토리 생성
#count_log 존재여부 확인
#count_log.txt 파일 생성, 있을 경우 이어쓰기
#예외처리 try except 꼭 사용하기
def makeLogFile():

    import os

    try:
        os.chdir('C:\wonGit\week6') # 위크6 까지 찾아들어옴
        if not os.path.exists('log') :
        #if not os.path.isdir('log) 랑 같음
            os.mkdir('log') #없으면 로그 디렉토리를 만들겠다.

        if not os.path.isfile('log\count_log.txt'):
            f = open('log/count_log.txt', 'w' , encoding='utf-8')
            f.write('기록시작\n')
            f.close()

        with open('log/count_log.txt', 'a' , encoding='utf-8') as f:
            import datetime
            for i in range(1,11):
                now = datetime.datetime.now() #현재시간
                str_now = now.strftime("%Y-%m-%d %H:%M:%S") #datetime을 string으로 형변환
                log_line = str_now+' '+str(i)+'값이 생성됨\n'
                f.write(log_line)


    except FileNotFoundError as e:
        print('파일 없음', e)
    except FileExistsError as e:
        print('파일 있음', e)
    except Exception as e:
        print('오류 발생', e)
    finally:
        print('종료')

makeLogFile()
