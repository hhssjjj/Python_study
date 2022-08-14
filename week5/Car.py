# 멤버 변수
cc = 0 # 엔진 cc
door = 0 # 문짝 개수
carType = None #문자값은 none이 초기값임.

class Car:
    cc = 0
    door = 0
    carType = None

    def __init__(self, cc, door, carType): #재정의했기때문에 set함수 필요없음
        self.cc = cc
        self.door = door
        self.carType = carType

    def display(self):
        print("자동차는 %d이고, 문짝은 %d개, 타입은 %s이다."%(self.cc, self.door, self.carType))

car1 = Car(2000, 4, "승용차") #객체 생성
car1.display()

car2 = Car(3600, 4, "SUV")
car2.display()
    