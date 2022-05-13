def remove_parentheses(s):
    s_list = list(s)
    b_indices = []
    e_indices = []
    for i in s_list:
        if i == '(':
            index = s_list.index('(')
            s_list[index] = '['
            b_indices.append(index)
        if i == ')':
            index = s_list.index(')')
            s_list[index] = ']'
            e_indices.append(index)
    for i in range(len(b_indices)):
        for i in range(b_indices[i], e_indices[i] + 1):
            s_list[i] = ''
    return ''.join(s_list)
