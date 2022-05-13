def how_much_water(water, load, clothes):
    result = ['Too much clothes' if load * 2 < clothes else 'Not enough clothes'
              if clothes < load else '']
    if result[0] == '':
        ans = water * 1.1 ** (clothes - load)
        return float("{:.2f}".format(ans))
    return result[0]
