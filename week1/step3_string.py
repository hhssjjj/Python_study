
# 문자열특징


oneLine = "this is one line string"
print(oneLine)

multiline = """this is
multi line
string"""

print(multiline)

# 줄내림2
multiline2 ="     this is\nmulti line\nstring     "
# find 찾는 문자열이 처음 나온 위치 반환 없을시에는 -1
print( multiline2.find('m'))

print( multiline2[8:13] )

# 공백제거 strip()
print(multiline2.lstrip())

# replace() -> 단어변경
# split

str3 = "사과/바나나/자몽"
print(str3.split('/'))

# 이까지 하고 2장 연습문제
