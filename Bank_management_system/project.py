class bank():
   def __init__(self):
      self.__password=None
      self.balance=0
      self.account_created=False
   def create_account(self):
      print("*********************************************")
      print("\t\twelcome to our bank")
      print("*********************************************")
      name=input("enter the name:")
      age=int(input("enter your age:"))
      ph=int(input("enter the phone number:"))
      import random
      acc_number=""
      for i in range(10):
         acc_number+=str(random.randint(0,9))
      print("------------------------------------------")
      print("\t\tname   :",name)
      print("\t\tage    :",age)
      print("\t\tphone number   :",ph)
      print("\t\taccount number :",acc_number)
      print("\t\tdeposite your initial amount")
      self.balance=int(input("enter the amount to deposite"))
      print("create your password")
      self.__password=int(input("enter the password"))
      self.account_created=True
      print("account created succesfully")
      print("---------------------------------------------")
   def deposite(self):
      print("***********************************************")
      password=int(input("enter the password"))
      if(password==self.__password):
         amount=int(input("enter the amount to deposite"))
         self.balance +=amount
         print(amount," deposite successfully")
         print("current balance is",self.balance)
      else:
         print("invalid password")
      print("*************************************************")

   def withdraw(self):
       print("#################################################")
       password=int(input("enter the password"))
       if(password==self.__password):
        amount=int(input("enter the amount to withdraw"))
        if(amount<=self.balance):
            self.balance -=amount
            print(amount," withdraw successfully")
            print("current balance is",self.balance)
        else:
           print("insufficiant balance")
       else:
         print("invalid password")
       print("#################################################")
   def check_balance(self):
    print("*****************************************************")
    password=int(input("enter the password"))
    if(password==self.__password):
         print("current balance is",self.balance)
    else:
         print("invalid password")
    print("*****************************************************")
   def password_change(self):
    print("------------------------------------------------------")
    self.__password=int(input("enter the new password"))
    print("password changed successfully")
    print("------------------------------------------------------")
   def menu(self):
       
       while True:
           
           if not self.account_created:
                print("\n1.create account")
                ch=int(input("enter the choice"))
                if ch==1:
                     self.create_account()
                else:
                  print("PLEASE CREATE ACCOUNT")
           else:
               print("1.creade account\n2.cash deposite\n3.cash withdraw\n4.balance inquery\n5.pin change\n6.exit")
               ch=int(input("enter the choice"))
               if ch==1:
                   print("account already created")
                   break

               elif ch==2:
                  self.deposite()
               elif ch==3:
                  self.withdraw()
               elif ch==4:
                  self.check_balance()
               elif ch==5:
                  self.password_change()
               elif ch==6:
                    break
               else:
                   print("invalid choice")
b1=bank()
b1.menu()
