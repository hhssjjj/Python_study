

def bankSystem():
    balance = 0 #잔액

    # 잔액확인
    def getBalance():

        print('잔액확인 =', balance)


    # 입금
    def deposit(money):
        #global balance
        nonlocal balance
        balance += money
        print('%d원이 입금되었습니다.'%money)


    # 출금  , 출금액이 잔액보다 크면 잔액이 부족합니다.
    def withdraw(money):
        #global balance
        nonlocal balance
        if balance > money:
            balance -= money
            print(format(money, "3,d"), '원이 출금되었습니다.')
        else:
            print('잔액부족')

    return getBalance, deposit, withdraw

getBalance, deposit, withdraw = bankSystem()

getBalance()
deposit(5000)
getBalance()
deposit(10000)
getBalance()
withdraw(10000)
getBalance()



#getBalance()

#deposit(50000)
#getBalance()

#deposit(70000)
#getBalance()

#withdraw(400000)
#getBalance()
