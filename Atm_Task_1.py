import time
time.sleep(5)
Password=1234
Balance = 10000
print("Welcome To Atm")
Pin=int(input("Enter Your Password 4 -Digits ****"))

if Password==Pin:
    while True:
        print("""
          1 --> Show the Balance
          2 --> Widthdraw the Amount
          3 --> Deposit the Money
          4 --> Exit
          """)
        try:
            Option = int(input("Choose The Correct Option"))
        except:
            print("Enter the VAlid Option")
        
        if Option==1:
            print(f'Current Balance is ${Balance}')

        if Option==2:
            print("===============================================")
            withdraw_amount = int(input("Enter Amount To withdraw"))
            print("===============================================")
            Balance = Balance-withdraw_amount
            print(f'Entered Amount to Withdraw{withdraw_amount}')
            print("===============================================")
            print(f'Remaining Balance{Balance}')
            print("===============================================")

        if Option==3:
            print("===============================================")
            Deposit_amount = int(input("enter the amount to Deposit"))
            print("===============================================")
            Balance=Balance+Deposit_amount
            print(f'deposited amount is ${Deposit_amount}')
            print("===============================================")
            print(f'total balance is ${Balance}')
            print("===============================================")
        if Option==4:
            print("===============================================")
            print('Thank You For Using')
            print("===============================================")
            break
else:
    print("Invalid Password/Pin")

   



