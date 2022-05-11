def recurrence(values):
    prev, count = 0, -1
    values = values[values.index(min(values)):]

    for i in range(len(values)):
        if values[i] > prev:
            count += 1
        else:
            count = 0
        prev = values[i]
        if count > 2:
            return True
    return False


