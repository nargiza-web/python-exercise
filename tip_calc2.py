bill= int(input('Total bill amount? '))
service = input ('Level of service? ')
split = int(input ('Split how many ways? '))
tip = 0
if service == 'good':
    tip = 0.2 * bill
elif service =='fair':
    tip = 0.15 * bill
elif service == 'bad':
    tip = 0.1 * bill
else :
    print ('type \'good\', \'fair\' or \'bad\' only')
print (f'Tip amount: ${tip}')
total = tip + bill
print (f'Total amount: ${total}')
amount = total / split
print (f'Amount per person: ${amount}')