a = int( input() )
b = int( input() )
c = int( input() )
x = int( input() )
y = int( input() )
z = int( input() )
m1 = int( a // x ) * int( b // y ) * int( c // z )
m2 = int( a // x ) * int( b // z ) * int( c // y )
m3 = int( a // y ) * int( b // a ) * int( c // z )
m4 = int( a // y ) * int( b // z ) * int( c // x )
m5 = int( a // z ) * int( b // a ) * int( c // y )
m6 = int( a // z ) * int( b // y ) * int( c // x )
if a >= x and b >= y and c >= z:
    if m1 > m2 and m1 > m3 and m1 > m4 and m1 > m5 and m1 > m6:
        print( m1 )
    elif m2 > m3 and m2 > m4 and m2 > m5 and m2 > m6:
        print( m2 )
    elif m3 > m4 and m3 > m5 and m3 > m6:
        print( m3 )
    elif m4 > m5 and m4 > m6:
        print( m4 )
    elif m5 > m6:
        print( m5 )
    else:
        print( m6 )
else:
    print( 0 )
