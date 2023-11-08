#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    numt = 0
    numd = 0
    for i in my_list:
        numt += i[0] * i[1]
        numd += i[1]

    return numt/numd
