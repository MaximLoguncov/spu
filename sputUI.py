#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gooey import Gooey, GooeyParser
import math


@Gooey(dump_build_config=True, program_name="Программа для определения направления на спутник")
def main():
    parser = GooeyParser(description='Данная программа предназначенна для расчета направления на спутник')

    parser.add_argument(
        'GeoShir',
        metavar='Введите широту места приема:',
        help='Значение в градусах',
        gooey_options={
            'validator': {
                'test': 'float(user_input)',
                'message': 'Must be between 2 and 14'
            }
        })

    parser.add_argument(
        'GeoDolq',
        metavar='Введите долготу места приема:',
        help='Значение в градусах',
        gooey_options={
            'validator': {
                'test': 'float(user_input)',
                'message': 'Must be between 2 and 14'
            }
        })

    parser.add_argument(
    'SpGeoDol',
    metavar='Введите долготу спутника: ',
    help='Значение в градусах, западная долгота вводится со знаком -',
    gooey_options={
        'validator': {
            'test': 'float(user_input)',
            'message': 'Must be between 2 and 14'
        }
    })


    args = parser.parse_args()

    #определяем азимут
    tan1 = float(math.tan((float(args.GeoDolq) - float(args.SpGeoDol)) * math.pi/180))

    sin1 = math.sin(float(args.GeoShir) * math.pi / 180)

    atan1 = math.atan(tan1 / sin1) * (180/math.pi)

    print('Азимут :',180 + float('{0:4.2f}'.format(atan1)) )



    #определяем угол места

    cos2 = math.cos((float(args.GeoDolq) - float(args.SpGeoDol))* math.pi / 180) * (math.cos((float(args.GeoShir))*math.pi/180)) - 0.151;

    sqrt2 = math.sqrt(1- (math.pow(math.cos((float(args.GeoDolq) - float(args.SpGeoDol)) * math.pi/180), 2 ) * math.pow(math.cos(float(args.GeoShir)*(math.pi/180)),2)));

    atan2 = math.atan(cos2 / sqrt2) * (180 / math.pi);


    print('Угол места :', float('{0:4.2f}'.format(atan2)) )



if __name__ == "__main__":
    main()
