def remove_smallest(numbers):
    num_list = numbers.copy()
    try:
        if len(num_list) == 1 or not num_list:
            return []
        check_similarity = \
            num_list.count(num_list[0])\
            == len(num_list)
        if check_similarity:
            return num_list
        mm = min(num_list)
        num_list.remove(mm)
        print(num_list)
    except IndexError:
        pass
