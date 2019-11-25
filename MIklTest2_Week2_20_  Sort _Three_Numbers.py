a, b, c = int( input() ), int( input() ), int( input() )
if a <= b <= c:
    a, b, c = a, b, c
elif a <= c <= b:
    a, b, c = a, c, b
elif a >= b >= c:
    a, b, c = c, b, a
elif a >= c >= b:
    a, b, c = b, c, a
elif a <= c >= b:
    a, b, c = b, a, c
elif a <= b >= c:
    a, b, c = c, a, b
print( a, b, c )

# print (-11//10)
# if a < b < c and a < c:
# print(a, b, c)
# Дано три числа. Упорядочите их в порядке неубывания.
# Программа должна считывать три числа a,b,c, затем
# программа должна менять их значения так, чтобы стали
# выполнены условия a≤b≤c, затем программа выводит тройку a,b,c.
