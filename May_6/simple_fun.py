def zero_and_one(s):
    s_list = list(s.strip(' '))
    for j in range(len(s)):
        try:
            i = j + 1
            if s_list[j] == ' ':
                continue
            if s_list[j] != s_list[i]:
                s_list[j] = s_list[i] = ' '
        except IndexError:
            continue
    s = ''.join(s_list)
    counter = [x for x in s if x != ' ']
    return len(counter)
