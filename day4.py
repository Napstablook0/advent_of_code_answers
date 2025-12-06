

with open("input4.txt", "r") as f:
    inp =  f.read().splitlines()



def isAccessible(map, x, y):
    if map[x][y] != "@": return False
    counter = 0

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i >= 0 and i < len(map) and j >= 0 and j < len(map[i]):
                if not (i == x and j == y):
                    if map[i][j] == "@":
                        counter += 1
    
    return counter < 4



test_map = ["@@@.@..@@.@@..@.@@@...@...@@@.@@..@..@@@@@@.@@.@@@.@@@@@@@@@@@@@......@@@@@@@@......@@.@@@@@@@.@.@@.@@@@@.@...@......@@@@@@@@@@@@.@@@@@@@",
            "@@@.@@@@@@@@.@@@@.@@@@.@.@.@.@@@..@..@@@@...@@@@@@@@.@@@.@@@@@@.@..@@@@@.@@.@.@.@@@@.@@@......@@@@@.@..@@@...@@@@@@@@@@.@.@@@@@@@@.@@@@..",
            "..@@@@.@.@.@@@.@@@@@..@@@@.@@@@..@@@.@.@@@...@@@@@..@@@@.@@@@@..@@@@@...@@..@.@@@@.@@.@@.@@.@@.@..@.@@@@@....@@@...@@.@.@@@@@.@.....@@.@@",
            ".@@@..@@.@.@@.@@@@@@..@@@.@@..@@@@...@@@.@@@.@@.@@@@@@.@@@@..@@@@@.@@@@@@@..@@....@@.@....@@@@@.@@.@@@..@@@@.@.......@@@@...@@@@.@..@..@@",
            "@@@..@..@@@@.@.@@@@@@..@@@@..@.@.@@@.@..@@@@@.@...@..@..@...@....@@..@@@...@@@@@.@.@........@..@@.@.@@...@@@@@.@@@@..@.@@@@...@..@@.@@..@"]


assert isAccessible(test_map, 0, 0) == True, "tests"
assert isAccessible(test_map, 2, 2) == False, "tests"
assert isAccessible(test_map, 3, 6) == False, "tests"
assert isAccessible(test_map, 4, 0) == True, "tests"
assert isAccessible(test_map, 1, 48) == False, "tests"
assert isAccessible(test_map, 0, 3) == False, "tests"


def countAccessibleRolls(map):
    counter = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if isAccessible(map, i, j):
                counter += 1

    return counter


def remove(map, i, j):

    if j+1 != len(map[i]):
        map[i] = map[i][:j] + "x" + map[i][j+1:]
    else:
        map[i] = map[i][:j] + "x"



test_map = ["..@@.@@@@.",
            "@@@.@.@.@@",
            "@@@@@.@.@@",
            "@.@@@@..@.",
            "@@.@@@@.@@",
            ".@@@@@@@.@",
            ".@.@.@.@@@",
            "@.@@@.@@@@",
            ".@@@@@@@@.",
            "@.@.@@@.@."]


remove(test_map, 9, 0)
remove(test_map, 1, 9)
remove(test_map, 2, 2)


assert test_map == ["..@@.@@@@.",
                    "@@@.@.@.@x",
                    "@@x@@.@.@@",
                    "@.@@@@..@.",
                    "@@.@@@@.@@",
                    ".@@@@@@@.@",
                    ".@.@.@.@@@",
                    "@.@@@.@@@@",
                    ".@@@@@@@@.",
                    "x.@.@@@.@."]


def countAndRemoveAccessibleRolls(map):
    counter = 0
    at_least_one = False
    for i in range(len(map)):
        for j in range(len(map[i])):
            if isAccessible(map, i, j):
                counter += 1
                at_least_one = True
                remove(map, i, j)

    return counter, at_least_one


test_map = ["..@@.@@@@.",
            "@@@.@.@.@@",
            "@@@@@.@.@@",
            "@.@@@@..@.",
            "@@.@@@@.@@",
            ".@@@@@@@.@",
            ".@.@.@.@@@",
            "@.@@@.@@@@",
            ".@@@@@@@@.",
            "@.@.@@@.@."]


assert countAccessibleRolls(test_map) == 13, "tests"



result1 = countAccessibleRolls(inp)

result2 = 0
continue_loop = True
while continue_loop:
    next_result, continue_loop = countAndRemoveAccessibleRolls(inp)
    result2 += next_result

print(result1)
print(result2)
