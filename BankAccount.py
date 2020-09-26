
class BankAccount:
  def __init__(self,name,deposit=0):
    self.deposit=deposit
    self.name=name
  def display(self):
    print(self.name)
    print(self.deposit) 
  def withdraw(self,x):
    self.deposit-=x
  def deposit(self,x):
    self.deposit+=x
 
