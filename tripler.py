def tripler(array):
    result = []
    for i in range(len(array)):
        num = array[i]
        multiple = num * 3
        result.append(multiple)
    return result