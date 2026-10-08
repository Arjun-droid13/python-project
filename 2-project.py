# bank management system
transaction = []
balance = 25000

def showbalance():
  print('Current balance: ',balance)

def depositemoney():
  global balance
  amount = int(input('Enter your amount: '))
  if amount <=0:
    print('Invalid amount')
    return
  balance += amount

  transaction.append(f'Deposited {amount}')
  print('money deposited successfully')
  print('current balance: ',balance)

def withdrawl():
  global balance
  withamount = int(input('Enter amount: '))
  if withamount <= 0 or withamount > balance: 
    print('Invalid amount')
    return
  balance -= withamount
  transaction.append(f'withdrawl {withamount}')
  print('money withdrawl successfully')
  print('available amount: ',balance)

def transactionshow():
  for i in range(len(transaction)):
    print(i+1 ,'->' ,transaction[i])

while True:
  print('=====main menu=====')
  print('1 -> check balance')
  print('2 -> deposite money')
  print('3 -> withdrawl money')
  print('4 -> transaction')
  print('5 -> exit')

  choice = int(input('Enter your choice: '))
  match choice:
    case 1:
      showbalance()
    case 2:
      depositemoney()
    case 3:
      withdrawl()
    case 4:
      transactionshow()
    case 5:
      print('Thnks for using bank management system')
      break
    case _:
      print('Invalid choice')
      continue
  