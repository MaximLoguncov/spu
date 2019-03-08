#сделано 8.03.19

import math


GeoShir = float(input('Введите широту места приема: '))
GeoDolq = float(input('Введите долготу места приема: '))
SpGeoDol = float(input('Введите долготу спутника: '))




#определяем азимут

tan1 = math.tan((GeoDolq - SpGeoDol) * math.pi/180)

sin1 = math.sin(GeoShir * math.pi / 180)

atan1 = math.atan(tan1 / sin1) * (180/math.pi)

print('Азимут : ',180 + atan1)


#определяем угол места

cos2 = math.cos((GeoDolq - SpGeoDol)* math.pi / 180) * (math.cos((GeoShir)*math.pi/180)) - 0.151;

sqrt2 = math.sqrt(1- (math.pow(math.cos((GeoDolq - SpGeoDol) * math.pi/180), 2 ) * math.pow(math.cos(GeoShir*(math.pi/180)),2)));

atan2 = math.atan(cos2 / sqrt2) * (180 / math.pi);

print('Угол места : ', atan2 )
