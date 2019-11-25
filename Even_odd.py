a, b, c = int( input() ), int( input() ), int( input() )
if a % 2 == 1 and b % 2 == 1 and c % 2 == 1:
    print( 'Все числа не четные' )
elif a % 2 == 1 and b % 2 == 0 and c % 2 == 0 \
        or a % 2 == 0 and b % 2 == 1 and c % 2 == 0 \
        or a % 2 == 0 and b % 2 == 0 and c % 2 == 1:
    print( 'Есть одно не четное число' )
elif a % 2 == 1 and b % 2 == 1 and c % 2 == 0 \
        or a % 2 == 0 and b % 2 == 1 and c % 2 == 1 \
        or a % 2 == 1 and b % 2 == 0 and c % 2 == 1:
    print( 'Есть два не четных числа' )
else:
    print( 'Все числа четные' )
