#187쪽

class Employee():

    def __init__(self, name, hire_type):
        self.name = name
        self.hire_type = hire_type
        self.salary = 0

    def pay_calc(self):
        print("이름:{}, 고용형태:{}, 급여:{}".format(self.name, self.hire_type, self.salary))


class Permanent(Employee):
    def __init__(self, name, pay, bonus):
        super().__init__(self.name, '정규직')
        self.salary = pay + bonus

class Temporary(Employee):
    def __init__(self, name, base, hour):
        super().__init__(self.name, '임시직')
        self.salary = base * hour

inputType = input("고용형태 입력 (정규직:p or 임시직:t) \n")
if inputType == "p":
    name = input('이름: ')
    pay = int(input('기본급: '))
    bonus = int(input('상여금: '))
    p = Permanent(name, pay, bonus)
    p.pay_calc()

elif inputType == 't':
    name = input('이름: ')
    base = int(input('시급: '))
    hour = int(input('시간: '))
    t = Temporary(name, base, hour)
    t.pay.calc()

