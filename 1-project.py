# hotel management system
rooms = ['single','double','deluxe','suite','premium']
price = [1500,2500,3500,5000,7000]
total = 0
bookedroom = []
booked = 0
name = input('Enter customer name: ')
number_days = 0
def showrooms():
  for i in range(5):
    print(i+1, '->' ,rooms[i], '-->' ,price[i])

def bookroom():
  global total
  global booked
  
  room_number = int(input('Enter your room number: '))
  if room_number <1 or room_number > 5:
    print('Invalid number')
    return
  number_days = int(input('Enter number of days: '))
  if number_days <= 0:
    print('Invalid days')
    return 

  booked = rooms[room_number-1]
  bookedroom.append(room_number)
  total = price[room_number-1] * number_days

  if room_number in bookedroom:
    print('Room is already booked')
    return

def summary():
  global total
  global booked

  print('=======BOOKING SUMMARY=======')
  print('customer: ',name)
  print('Room', booked)
  print('Nights: ',number_days)
  print('Total: ',total)

while True:
  print('1.show room')
  print('2.book room')
  print('3.summary')
  print('4.exit')

  choice = int(input('Enter your choice: '))

  match choice:
    case 1:
      showrooms()
    case 2:
      bookroom()
    case 3:
      summary()
    case 4:
      print('Thanks for using hotel management system')
      break
    case _:
      print('Invalid choice')
      continue
