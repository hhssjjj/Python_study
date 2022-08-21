
seq = 0 #전역변수

class Memo:
    no = 0
    title = ''
    content = ''

    def __init__(self  , title , content):
        global seq
        seq += 1
        self.no = seq

        self.title = title
        self.content = content

    def setContent(self ,content):
        self.content = content

    def getContent(self):
        return self.content

class MemoList:
    memo_list = []
    def insertMemo(self,title ,content):
        self.memo_list.append(Memo(title,content))

    def selectMemo(self, s_word , type):
        if type == 1:
            for m in self.memo_list:
                if m.no == s_word:
                    print('===============================')
                    print('번호:', m.no)
                    print('제목:', m.title)
                    print('내용:', m.content)
        elif type ==2:
            for m in self.memo_list:
                if s_word in m.title:
                    print('===============================')
                    print('번호:', m.no)
                    print('제목:', m.title)
                    print('내용:', m.content)
        elif type == 3:
            for m in self.memo_list:
                if s_word in m.content:
                    print('===============================')
                    print('번호:', m.no)
                    print('제목:', m.title)
                    print('내용:', m.content)

    def getMemoList(self):
        for m in self.memo_list:
            print('===============================')
            print('번호:', m.no)
            print('제목:', m.title)
            print('내용:', m.content)

while True:
    type = input('메모입력:1, 메모선택:2, 메모목록:3 , 종료:0 \n')
    if type == '1':
        memo = MemoList()
        while True:
            title = input('제목을 입력하세요 \n')
            content = input('내용을 입력하세요 \n')
            # memo = MemoList()
            memo.insertMemo(title,content)
            yn = input('다음 메모를 입력하시겠습니까 Y/N \n')
            if yn == 'y' or yn == 'Y':
                continue
            elif yn == 'n' or yn =='N':
                break
            else:
                print('잘못된 값입니다.')
                break
    elif type == '2':
        # memo = MemoList()
        while True:
            search_type = int(input('1:메모번호 , 2:제목검색 , 3:내용검색 , 0:이전단계로 \n' ))
            if search_type == 1:
                s_word = input('확인할 메모 번호를 입력하세요\n')
                memo.selectMemo(s_word, 1)
            elif search_type == 2:
                s_word = input('검색할 제목을 입력하세요\n')
                memo.selectMemo(s_word,2)
            elif search_type == 3:
                s_word = input('검색할 내용을 입력하세요\n')
                memo.selectMemo(s_word,3)
            else:
                break

    elif type == '3':
        memo.getMemoList()
    elif type == '0':
        break






