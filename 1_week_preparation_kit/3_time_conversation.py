import math
import os
import random
import re
import sys

def timeConversion(s):
    hor_str = s[0:2]
    min_str = s[3:5]
    seg_str = s[6:8]
    am_pm_str = s[8:10]

    hor_int = int(hor_str)

    if am_pm_str == 'AM':
        if hor_int == 12:
            hor = '00'
        elif hor_int < 12:
            hor = '0'+ str(hor_int)
        else:
            hor_int -= 12
            hor = str(hor_int)
    else:
        if hor_int == 12:
            hor = '12'
        else:
            hor_int += 12
            hor = str(hor_int)

    print(f'{hor}:{min_str}:{seg_str}')


s = input()

result = timeConversion(s)
