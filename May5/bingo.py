def bingo(array):
    bingo_list = {2, 9, 14, 7, 15}
    setArray = set(array)
    return 'WIN' if bingo_list.issubset(setArray) else 'LOSE'
