bill= int(input('Total bill amount?'))
service = input ('Level of service?')
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