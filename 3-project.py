# super market management system
product = ['rice','sugar','milk','bread','biscuits']
price = [60,45,60,40,30]
total = 0
products = []
quantities = []
prices = []
name = input('Enter customer name: ')
def showproduct():
  for i in range(5):
    print(i+1 , '->' , product[i] , '->' , price[i])

def addproduct():
  global total
  global products
  global quantities
  global prices
  while True:
   productnumber = int(input('Enter product number: '))
   if productnumber <= 0 or productnumber > 5:
     print('Invalid product')
     continue
   quantity = int(input('Enter quantity: '))
   if quantity <=0:
     print('Invalid quantity')
     continue
   print(product[productnumber - 1] , 'added successfully !')

   products.append(product[productnumber - 1])
   quantities.append(quantity)
   prices.append(price[productnumber-1])
   total += price[productnumber-1] * quantity
   ask = input('Do you want to add another product: ')
   if ask =='no':
     break

def showbill():
  global products
  global total
  global quantities
  global prices

  print('======Bill summary======')
  print('Customer name: ',name)
  for i in range(len(products)):
   print(products[i] , '->' , quantities[i] , '->' , prices[i])
  print('Total: ',total)

while True:
  print('1->Show product')
  print('2->Add product')
  print('3->Show bill')
  print('4->Exit')

  choice = int(input('Enter your choice: '))
  match choice:
    case 1:
       showproduct()
    case 2:
      addproduct()
    case 3:
       showbill()
    case 4:
      print('Thanks for choice this system')
      break
    case 5:
      print('Invalid choice ')
      continue