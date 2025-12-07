

with open("input7.txt", "r") as f:
    inp = f.read().splitlines()


# S =  inp[0][70]



def _moveDownward(mat:  list[str], x: int, y: int, deja_faits: dict):
    """returns the number of times the beam splited"""
    n  = len(mat)
    m =  len(mat[0])
    assert x >= 0 and x < m, "x has to be a correct coordinate"
    assert y >= 0 and y < n, "y has to be a correct coordinate"


    if (x, y) in deja_faits.keys():
        return 0

    if (mat[y][x] == "." or mat[y][x] == "S") and y+1 >= 0 and y+1 < n:
        next = _moveDownward(mat, x, y+1, deja_faits)
        deja_faits[(x, y+1)] = next
        
        return next
    elif mat[y][x] == "^":
        next1 = _moveDownward(mat, x-1, y, deja_faits)
        next2 = _moveDownward(mat, x+1, y, deja_faits)
        deja_faits[(x-1, y)] = next1
        deja_faits[(x+1, y)] = next2

        return 1 + next1 + next2
    else:
        return 0
    


def moveDownward(mat, x, y):
    deja_faits = {}
    return _moveDownward(mat, x, y, deja_faits)


def _moveDownwardLevel2(mat:  list[str], x: int, y: int, deja_faits: dict):
    """returns the number of paths the beam can take"""
    n  = len(mat)
    m =  len(mat[0])
    assert x >= 0 and x < m, "x has to be a correct coordinate"
    assert y >= 0 and y < n, "y has to be a correct coordinate"


    if (x, y) in deja_faits.keys():
        return deja_faits[(x, y)]

    if (mat[y][x] == "." or mat[y][x] == "S") and y+1 >= 0 and y+1 < n:
        next = _moveDownwardLevel2(mat, x, y+1, deja_faits)
        deja_faits[(x, y+1)] = next
        
        return next
    elif mat[y][x] == "^":
        next1 = _moveDownwardLevel2(mat, x-1, y, deja_faits)
        next2 = _moveDownwardLevel2(mat, x+1, y, deja_faits)
        deja_faits[(x-1, y)] = next1
        deja_faits[(x+1, y)] = next2

        return next1 + next2
    else:
        return 1
    


def moveDownwardLevel2(mat, x, y):
    deja_faits = {}
    return _moveDownwardLevel2(mat, x, y, deja_faits)



with open("input7_test.txt", "r") as f:
    inp_test = f.read().splitlines()


assert moveDownwardLevel2(inp_test, 7, 0) == 40, "tests"




result1 = moveDownward(inp, 70, 0)
result2 = moveDownwardLevel2(inp, 70, 0)
print("level1 :", result1)
print("level2 :", result2)
