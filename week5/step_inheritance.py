class Person(object): # 부모 클래스 Person 선언
    # 클래스 변수 생략가능(생성자에서 초기화 할 경우)
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def about_me(self): # 메서드 선언
        print("제 이름은", self.name, "이고요, 제 나이는", str(self.age), "살이며,",self.gender, "입니다.")

Person1 = Person('아이유','30','여자').about_me()

#부모 클래스 Person으로부터 상속
class Employee(Person):
    def __init__(self, name, age, gender, salary, hire_date):
        # 부모의 생성자 호출 (부모로부터 인스턴스를 받아옴)
        super().__init__(name, age, gender)
        self.salary = salary
        self.hire_date = hire_date

    #메서드 재정의(overriding)
    def about_me(self):
        super().about_me()
        print("제 기본급여는",self.salary, "원이고, 제 입사일은",self.hire_date, "입니다.")
    def pay_calc(self):
        return self.salary



# employee1 = Employee('아이유', '30', '여자', 5000000, '20090604').about_me() # 부모로 부터 상속받아서 메서드 없어도 어바웃미 쓸수 있음.


class permanent(Employee):
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name, age, gender, salary, hire_date)
    def pay_calc(self, base, bonus):
        self.salary = base + bonus
        print('총 수령액:', format(self.salary))

p1 = permanent("주한솔","28", "여자", 3000000,"20200421")
p1.about_me()
p1.pay_calc(2000000, 1500000)

class Temporary(Employee):
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name, age, gender, salary, hire_date)

    def pay_calc(self, time):
        self.salary = self.salary * time
        print('총 수령액:', format(self.salary))

t1 = Temporary("하하", "30", "남자",10000, "20100708")
t1.about_me()
t1.pay_calc(5)



class Parent:
    # 생성자 : 객체 + 초기화
    def __init__(self, name, job):
        self.name = name
        self.job = job

    # 멤버 함수(메서드)
    def display(self):
        print('name: {}, job : {}'.format(self.name, self.job))

# 부모 클래스 객체 생성
p = Parent('홍길동', '회사원')
p.display()

class Children(Parent):

    def __init__(self, name, job, gender):
        super().__init__(name, job)
        self.gender = gender
    # 메서드 재정의
    def display(self):
        print('name: {}, job : {}, gender : {}'.format(self.name, self.job, self.gender))


# 자식 클래스 객체 생성
chil = Children("이순신", "해군 장군", "남자")
chil.display()





