coin = 0
print(f' You have {coin} coins ')
answer = input ('Do you want another?')

while answer == 'yes':
    coin += 1
    print (f'You have {coin} coins')
    answer = input ('Do you want another? ')
print ('Bye')