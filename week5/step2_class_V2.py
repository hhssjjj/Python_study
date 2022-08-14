#(1) 생성자 이용 멤버변수 초기화
class multiply:
    #멤버 변수
    x = y = 0

    # 생성자 : 초기화
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def mul(self):
        return self.x * self.y

    # 소멸자
    def __del__(self):
        del self.x
        del self.y


obj = multiply(10,20)
print('곱셈', obj.mul())