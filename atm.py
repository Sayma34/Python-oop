class Atm:
    def __init__(self):
       self.pin = ""   #creating variable
       self.balance = 0  #creating variable
       self.menu()
       
    def menu(self):
        user_input = input(""" 
                           Hello how would you like to proceed?
                           1. Enter 1 to create pin
                           2. Enter 2 to deposit
                           3. Enter 3 to withdraw
                           4. Enter 4 to check balance
                           5. Enter 5 to exit""") 
        
        if user_input == "1":
            #print("Create pin")
            self.create_pin()
        elif user_input == "2":
            #print("deposit")
            #rather than printing it, im just callin the func
            self.deposit()
        elif user_input == "3":
            #print("Withdraw")
            self.withdraw()
        elif user_input == "4":
            #print("balance")
            self.check_balance()
        else:
            print("dafa h o jao")
            
    def create_pin(self): #
        self.pin = input("Enter your pin") # user amk ja dcche seta line-3 er var e pathai dcche
        print("pin set") # print out kre dlam
        
    def deposit(self):
        temp = input(" enter pin") # frst atm will ask u a pin that will be kept in temp var
        if temp == self.pin: # now comparing the input pin with the actual pin
            amount = int(input("enter amount")) #now asking user the amount. ei amount ta ami store krtesi in a var named 'amount'. and typecasting it into int as i would get string.
            self.balance = self.balance + amount # 
            print(" deposit successful")
        else:
             print(" invalid pin")   
             
    def withdraw(self):
        temp = input(" enter pin")  
        if temp == self.pin:
            amount = int(input("enter amount"))
            if amount < self.balance:
                self.balance = self.balance - amount  
                print("operation successful")   
            else:
                print("insufficient funds")  
        else:
            print("Invlid pin") 
            
    def check_balance(self):
        temp = input(" enter pin")  
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid pin")     
            
obj1 = Atm()
obj1.create_pin()
obj1.deposit()
obj1.withdraw()
obj1.check_balance()            
        
