# 다형성

#(1) 부모 클래스
class Flight:

    # 부모 원형 함수
    def fly(self):
        print('날다, fly 원형 메서드')

#(2) 자식 클래스 : 비행기
class Airplane(Flight):

    #함수 재정의
    def fly(self):
        print('비행기가 날다.')

#(2) 자식 클래스 : 새
class Bird(Flight):

    # 함수 재정의
    def fly(self):
        print('새가 날다.')

#(2) 자식 클래스 : 종이비행기
class PaperAirplane(Flight):

    # 함수 재정의
    def fly(self):
        print('종이비행기가 날다.')

flight = Flight() # 부모 클래스 객체
air = Airplane() #자식 1 클래스 객체
bird = Bird() #자식 2 클래스 객체
paper = PaperAirplane() #자식 3 클래스 객체

flight.fly()

flight = air # 부모 클래스를 자식으로 지정해놓음
flight.fly() # 부모가 자식형으로 형변환 (자식이 부모형으로는 안됨, 부모가 더 큰 그릇)

flight = bird
flight.fly()

flight = paper
flight.fly()
