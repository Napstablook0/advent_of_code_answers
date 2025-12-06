import time




with open("input5.txt", "r") as f:
    inp =  f.read().splitlines()


separator_index = inp.index("")


inp_fresh = inp[:separator_index]
inp_stock = inp[separator_index+1:]



def convertToTuple(id_range: str):
    index_sep = id_range.index("-")
    return int(id_range[:index_sep]), int(id_range[index_sep+1:])


assert convertToTuple("133-145") == (133, 145)
assert convertToTuple("3-9") == (3, 9)
assert convertToTuple("1-1") == (1, 1)



def convertToListOfTuples(list_range_id):
    list_fresh = []
    for range_id in list_range_id:
        list_fresh.append(convertToTuple(range_id))
    return list_fresh


assert convertToListOfTuples(["133-145", "3-9", "1-1"]) == [(133, 145), (3, 9), (1, 1)], "tests"


def isIdInRange(id, range_tuple):
    start, finish = range_tuple
    return int(id) in range(start, finish + 1)


assert isIdInRange(13, (1, 5)) == False, "tests"
assert isIdInRange(13, (12, 13)) == True, "tests"
assert isIdInRange(13, (13, 14)) == True, "tests"
assert isIdInRange(4, (1, 5)) == True, "tests"


def countIdsInRange(list_ids, list_range_tuple):
    counter = 0
    for id in list_ids:
        was_found = False

        for range_tuple in list_range_tuple:
            
            if isIdInRange(id, range_tuple) and not was_found:
                was_found = True
                counter += 1
    
    return counter


assert countIdsInRange([1, 2, 4, 7, 12], ([(2, 4), (11, 12), (2, 3), (1, 2)])) == 4, "tests"



def add(L: list, value):
    """adds a number to a sorted list if it wasnt already in it, returns True if it was aleady in it"""
    
    n= len(L)
    i = -1
    j = n
    
    while abs(i - j) != 1:
        m = (i+j)//2

        if L[m] == value:
            return True
        elif L[m] < value:
            i = m
        else:
            j = m

    if j < n and L[j] == value:
        return True
    else:
        L.insert(j, value)
        return False






list_test = [1, 2, 3]
assert add(list_test, 15) == False, "tests"
assert list_test == [1, 2, 3, 15], "tests"
list_test = []
assert add(list_test, 4) == False, "tests"
assert list_test == [4]
list_test = [1]
assert add(list_test, 0) == False, "tests"
assert list_test == [0, 1], "tests"
list_test = [1,2]
assert add(list_test, 4) == False, "tests"
assert list_test == [1, 2, 4], "tests"
list_test = [1, 2, 3]
assert add(list_test, 4) == False, "tests"
assert list_test == [1, 2, 3, 4], "tests"
list_test = [1, 2, 3]
assert add(list_test, 0) == False, "tests"
assert list_test == [0, 1, 2, 3], "tests"
list_test = [1, 2, 4]
assert add(list_test, 3) == False, "tests"
assert list_test == [1, 2, 3, 4], "tests"
list_test = [1, 3, 4]
assert add(list_test, 2) == False, "tests"
assert list_test == [1, 2, 3, 4], "tests"
list_test = [1, 3, 4, 7, 9, 12, 13, 14, 18, 21, 23]
assert add(list_test, 15) == False, "tests"
assert list_test == [1, 3, 4, 7, 9, 12, 13, 14, 15, 18, 21, 23], "tests"
list_test = [1, 3, 4, 7, 9, 12, 13, 14, 18, 21, 23]
assert add(list_test, 17) == False, "tests"
assert list_test == [1, 3, 4, 7, 9, 12, 13, 14, 17, 18, 21, 23], "tests"

list_test = [1, 2, 3]
assert add(list_test, 3) == True, "tests"
assert list_test == [1, 2, 3], "tests"
list_test = [1]
assert add(list_test, 1) == True, "tests"
assert list_test == [1], "tests"
list_test = [1,2]
assert add(list_test, 2) == True, "tests"
assert list_test == [1, 2], "tests"
list_test = [1, 2, 3]
assert add(list_test, 1) == True, "tests"
assert list_test == [1, 2, 3], "tests"
list_test = [1, 2, 3]
assert add(list_test, 2) == True, "tests"
assert list_test == [1, 2, 3], "tests"
list_test = [1, 2, 4]
assert add(list_test, 4) == True, "tests"
assert list_test == [1, 2, 4], "tests"
list_test = [1, 3, 4]
assert add(list_test, 3) == True, "tests"
assert list_test == [1, 3, 4], "tests"
list_test = [1, 3, 4, 7, 9, 12, 13, 14, 18, 21, 23]
assert add(list_test, 9) == True, "tests"
assert list_test == [1, 3, 4, 7, 9, 12, 13, 14, 18, 21, 23], "tests"
list_test = [1, 3, 4, 7, 9, 12, 13, 14, 18, 21, 23]
assert add(list_test, 21) == True, "tests"
assert list_test == [1, 3, 4, 7, 9, 12, 13, 14, 18, 21, 23], "tests"



def isInList(L, value):
    """returns True if a value is in a sorted list"""

    n = len(L)
    i = -1
    j = n
        
    while abs(i - j) != 1:
        m = (i+j)//2

        if L[m] < value:
            i = m
        elif L[m] > value:
            j = m
        else:
            return True
    return False


assert isInList([1, 2, 3], 1) == True, "tests"
assert isInList([], 1) == False, "tests"
assert isInList([1], 1) == True, "tests"
assert isInList([1, 2], 1) == True, "tests"
assert isInList([1, 2], 2) == True, "tests"
assert isInList([1, 2, 3], 0) == False, "tests"
assert isInList([1, 2, 3], 3) == True, "tests"
assert isInList([1, 2, 3], 2) == True, "tests"
assert isInList([1, 2, 3, 14, 17, 18, 19, 20, 21, 33, 37], 14) == True, "tests"
assert isInList([1, 2, 3, 14, 17, 18, 19, 20, 21, 33, 37], 32) == False, "tests"
assert isInList([1, 2, 3, 14, 17, 18, 19, 20, 21, 33, 34, 37], 32) == False, "tests"


def countFreshIds(list_range_tuple:  list[tuple[int]]):

    list_range_tuple.sort(key=lambda a: a[0])
    counter = 0
    list_fresh = []
    
    for range_tuple in list_range_tuple:
        start, finish = range_tuple



    return counter

assert countFreshIds([(2, 4), (11, 12), (2, 3), (1, 2)]) == 6, "tests"
assert countFreshIds([(2, 11), (11, 12), (2, 3), (1, 2)]) == 12, "tests"
assert countFreshIds([(2, 4), (11, 12), (2, 3), (1, 2), (44, 44)]) == 7, "tests"
assert countFreshIds([(2, 4), (11, 12), (2, 3), (1, 2), (11, 13)]) == 7, "tests"



list_range_id = convertToListOfTuples(inp_fresh)
print(countIdsInRange(inp_stock, list_range_id))
print(countFreshIds(list_range_id))

