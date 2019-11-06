start1 = int( input() )
finish1 = int( input() )
start2 = int( input() )
finish2 = int( input() )
answer = start1 <= finish2 and start2 <= finish1  # Условие проще
# isS1in2 = start2 <= start1 <= finish2 #начало первого отрезка во втором
# isF1in2 = start2 <= finish1 <= finish2
# isS2in1 = start1 <= start2 <= finish1
# isF2in1 = start1 <= finish2 <= finish1
# answer = isS1in2 or isF1in2 or isS2in1 or isF2in1
print( answer )
# Рассмотрим задачу о пересечении двух длительных по времени событий.
# Оба события характеризуются двумя числами - годами начала и конца.
# Необходимо определить, пересекались ли события во времени,
# при этом если одно событие началось в тот год,
# когда закончилось другое - они считаются пересекающимися.
