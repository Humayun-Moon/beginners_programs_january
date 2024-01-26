balance = 1000
print("""
Welcome to ATM Machine
      
Choose Transaction

1. BALANCE
2. WITHDRAW            
3. DEPOSIT
4. EXIT                 

""")
while True:
    option = input("Enter Transaction want to : ")
    if option.isdigit():
        option = int(option)
        

    if (option == 1):
        print(f"Your account balance is : {balance}")
    elif (option == 2):
        withdraw = float(input("Enter amount to withdraw: "))
        if (balance > withdraw):
            total = balance - withdraw
            print(f"Successfully withdrow is: {withdraw}")
            print(f"Your remain balance is : {total} ")    
        else:
            print("Insufficient Balance")
            print(f"Your balance is : {balance}")
            print(f"You wanted to withdraw {withdraw}")  
    elif (option == 3):
        diposit = float(input("Enter Diposit amount: "))        
        total_balance = balance + diposit
        print(f"Successfully Diposit is: {diposit}")
        print(f"Your current balance is: {total_balance}")
    elif(option == 4):
        exit()
    else:
        print("Oppops! Not selected any Transaction")
        continue

    
