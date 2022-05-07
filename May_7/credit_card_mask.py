# return masked string
def maskify(cc):
    cc_list =[c for c in cc]
    try:
        for j in range(len(cc) - 4):
            cc_list[j] = '#'
    except IndexError:
        pass
    return ''.join(cc_list)

# Good code:
# def maskify(cc):
#     return "#"*(len(cc)-4) + cc[-4:]
