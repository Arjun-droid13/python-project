
# Car Rental Management System

name = input('Enter customer name: ')

car = ['swift', 'baleno', 'creta', 'thar', 'fortuner']
price = [1500, 2000, 3000, 4000, 6000]

total = 0
rent = []
days = []
bookedcars = []

def showcars():
    for i in range(5):
        print(i + 1, '-->', car[i], '-> ₹', price[i], '/day')

def bookcar():
    global total

    while True:
        carnum = int(input('Enter car number: '))

        if carnum <= 0 or carnum > 5:
            print('Invalid choice')
            continue

        day = int(input('Enter number of days: '))

        if day <= 0:
            print('Invalid number of days')
            continue

        bookedcars.append(car[carnum - 1])
        prices = price[carnum - 1] * day

        days.append(day)
        rent.append(prices)
        total += prices

        print('Car booked successfully!')

        choice = input('Do you want to add another car? yes/no: ')

        if choice == 'yes':
            continue
        elif choice == 'no':
            break
        else:
            print('Wrong choice')
            break

def showbill():
    print('\n===== BILL SUMMARY =====')
    print('Customer:', name)

    for i in range(len(bookedcars)):
        print('\nCar:', bookedcars[i])
        print('Days:', days[i])
        print('Rent: ₹', rent[i])

    print('\nTotal rent: ₹', total)

showcars()
bookcar()
showbill()