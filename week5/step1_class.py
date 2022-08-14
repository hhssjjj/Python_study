
# def calc_func(a,b):
#     x = a
#     y = b
#
#     def plus():
#         p = x + y
#         return p
#     def minus():
#         m = x - y
#         return m
#
#     return plus, minus
#
# p, m = calc_func(5,10)
# print('plus =', p())
# print('minus =', m())

class Student:
    # 멤버변수(member variable)
    name = ''
    major = ''
    grade = ''
    subject = dict()

    # 생성자 : 기본적으로 자동생성
    def __init__(self):
        pass

    # 재정의된 생성자 : 멤버변수 초기화 해줌
    def __init__(self, name, major, grade):
        self.name = name
        self.major = major
        self.grade = grade
        self.subject = dict()


    # method 함수
    # 값을 지정하는 set 함수 -> 기본생성자 하면 set함수 만들어야함.
    def setName(self, t_name):
        self.name = t_name

    def setMajor(self, major):
        self.major = major

    def setGrade(self, grade):
        self.grade = grade

    def setSubject(self, key, value):
        self.subject[key] = value
        #self.subject.__setitem__(key,value) -> magic함수로 둘중에 하나 사용하면 됨.


    # get 함수
    def getName(self):
        return self.name

    def display(self):
        print("학생명:{},학과:{},학년{}".format(self.name, self.major, self.grade))

    def getSubject(self):
        for i in self.subject :
            print(i, end=',')
        print()



#인스턴스 생성
# st1 = Student()
# st1.setName('나꼼꼼')
# st1.setMajor('컴퓨터공학과')
# st1.setGrade('1학년')
# print(st1.getName())
# st1.display()
#
# st2 = Student()
# st2.setName('왕지락')
# st2.display()


st3 = Student('아이유', '방송연예과','2학년')
st3.display()

st4 = Student('강호동', '개그과', '4학년')
st4.display()

st5 = Student('조수미', '성악과', '4학년')
st5.setSubject('소프라노', 100)
st5.setSubject('바리톤', 90)
st5.setSubject('째즈', 200)
st5.setSubject('팝', 80)
st5.display()
st5.getSubject()

st6 = Student('하하', '개그과', '4학년')
st6.setSubject('예능', 100)
st6.setSubject('개그', 90)
st6.setSubject('노래', 200)
st6.setSubject('버라이어티', 80)
st6.display()
st6.getSubject()
