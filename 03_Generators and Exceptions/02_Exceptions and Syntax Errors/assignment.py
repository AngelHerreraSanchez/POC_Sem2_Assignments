try:
    value_1= int(input('Enter a number: '))
    value_2= int(input('Enter another number: '))
    print('If divided with each other then the out come will be', value_1/value_2)

except ZeroDivisionError: 
    print('You provided a 0 and division with 0 is not possible')



    