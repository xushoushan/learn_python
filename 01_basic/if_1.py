#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# birth_year=int(input('birth_year:'))
# if birth_year<2000:
#     print('00前')
# else:
#     print('00后')

height = 1.75
weight = 80.5
bmi = weight/(height*height)
if bmi<18.5:
   print('过轻')
elif bmi<25:
   print('正常')
elif bmi<28:
   print('过重')
elif bmi<32:
   print('肥胖')
else:
   print('严重肥胖')