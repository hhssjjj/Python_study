
class Account:
    balance = 0
    accName = '' #은닉 (private) -> accName 으로 다 바꿔주면 아예 실행이 안됨.
    accNo = None #계좌번호

    # 생성자 : 초기화
    def __init__(self, bal, name, no):
        self.balance = bal
        self.accName = name
        self.accNo = no


#잔액 확인
    def getBalance(self):

         print("계좌{}({})의 현재 잔액은 {}원 입니다.".format(self.accNo, self.accName, self.balance))


        # 입금
    def deposit(self, money):
        # 마이너스 금액 걸러내기
        if money < 0:
            print('금액확인바람')
            return #아래쪽 코드 실행안함.

        self.balance += money
        print(format(money, "3,d"), '원이 입금되었습니다.')


        # 출금  , 출금액이 잔액보다 크면 잔액이 부족합니다.
    def withdraw(self, money):

        if self.balance > money:
            self.balance -= money
            print(format(money, "3,d"), '원이 출금되었습니다.')
        else:
            print('잔액이 부족합니다.')
            return


acc1 = Account(20000, '한솔', '1004')

print(acc1.accName)

acc1.getBalance()
acc1.deposit(50000)
acc1.getBalance()
acc1.withdraw(5000)
acc1.getBalance()

acc2 = Account(50000, '메롱', '8888')
acc2.getBalance()
acc2.deposit(20000)
acc2.getBalance()
acc2.withdraw(300000)
acc2.getBalance()

