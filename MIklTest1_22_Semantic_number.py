v = int( input() )
a = v // 1000  # тысячи
s = v // 100 % 10  # сотни
d = v // 10 % 10  # десятки
f = v % 10  # деницы
t = (a - f) * (a - f) + (s - d) * (s - d) + 1
print( a )
print( s )
print( d )
print( f )
print( t )
# подсказка: разбейте введённое четырёхзначное
# число на 4 (тясячи, сотни, десятки, еденицы).
# Тогда всё станет проще
