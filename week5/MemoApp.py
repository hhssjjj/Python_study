
class Memo:
    title = ''
    content = ''
    # 멤버 변수 재정의 생성
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def setContent(self, content):
        self.content = content

    def getContent(self):  #값을 보여주는거
        return self.content

class MemoList:
    memo_list = []

    def createMemo(self, title, content):
        self.memo_list.append(Memo(title, content))

Type = input("메모입력:1, 종료:0 \n ")

while True:
    if Type == '1':
        title = input('제목을 입력하세요 \n ')
        content = input('내용을 입력하세요 \n ')
        memo1 = MemoList()
        memo1.createMemo(title, content)
        yn = input('다음 메모를 입력하시겠습니까? Y/N \n ' )
        if yn == 'y' or yn == 'Y':
            continue
        elif yn == 'n' or yn == 'N':
            break
        else:
            print('잘못된 값 입니다.')


    elif type == '0':
        break