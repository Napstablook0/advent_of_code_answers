


with open("input6.txt", "r") as f:
    inp_raw = f.read().splitlines()


inp = [None for _ in range(len(inp_raw))]
for i in range(len(inp_raw)):
    inp[i] = inp_raw[i].split()


mat_test = [["123", "328",  "51", "64"] ,
            ["45", "64", "387", "23"], 
            ["6", "98", "215", "314"],
            ["*", "+", "*", "+"]]

def calculateProblem(mat, i):

    if mat[-1][i] == "+":
        result = 0
        for j in range(len(mat)-1):
            result += int(mat[j][i])
    else:
        result =  1
        for j in range(len(mat)-1):
            result *=  int(mat[j][i])

    return result


assert calculateProblem(inp, 0) == 400200, "tests"
assert calculateProblem(inp, 1) == 1355, "tests"
assert calculateProblem(inp, -1) == 1261260, "tests"


def getIndexInRaw(mat, i):
    counter = -1
    j = -1
    while counter != i:
        j += 1
        if mat[-1][j] ==  "+" or mat[-1][j] == "*":
            counter += 1
        
    return j


assert getIndexInRaw(inp_raw, 3) == 11, "tests"
assert getIndexInRaw(inp_raw, 0) == 0, "tests"
assert getIndexInRaw(inp_raw, 1) == 3, "tests"
assert getIndexInRaw(inp_raw, 6) == 20, "tests"



def convert(inp, list_numbers, i):

    n = max([len(value) for value in list_numbers])
    list_converted = []

    index_left = getIndexInRaw(inp, i)
    index_right = index_left + n - 1

    for i in range(len(list_numbers)):
        list_numbers[i] = inp[i][index_left:index_right+1]

    for i in range(n):
        converted_number = ""

        for j in range(len(list_numbers)):

            if list_numbers[j][i] != " ":
                converted_number += list_numbers[j][i]

        list_converted.append(int(converted_number))

    return list_converted


assert convert(inp_raw, ["8", "75", "23", "29"], 0) == [722, 8539],  "tests"
assert convert(inp_raw, ["797", "142", "395", "21"], 1) == [713, 9492, 7251],  "tests"
assert convert(inp_raw, ["34", "794", "753", "161"], 2) == [771, 3956, 4431],  "tests"
assert convert(inp_raw, ["831", "634", "37", "6"], 8) == [86, 333, 1476],  "tests"


def prod(list_numbers):
    product = 1
    for value in list_numbers:
        product *= value
    return product


assert prod([1, 2, 3, 4]) == 24, "tests"
assert prod([1, 2, 4]) == 8, "tests"
assert prod([1, 2, 3]) == 6, "tests"
assert prod([1, 2, 3, 4, 3]) == 72, "tests"
assert prod([559, 5894]) == 3294746, "tests"


def calculateProblemLevel2(inp, mat, i):

    if mat[-1][i] == "+":

        list_numbers = []
        for j in range(len(mat)-1):
            list_numbers.append(mat[j][i])


        list_converted_numbers = convert(inp, list_numbers, i)
        result = sum(list_converted_numbers)
    else:

        list_numbers = []
        for j in range(len(mat)-1):
            list_numbers.append(mat[j][i])

        list_converted_numbers = convert(inp, list_numbers, i)
        result = prod(list_converted_numbers)
    
    return result


assert calculateProblemLevel2(inp_raw, inp, 0) == 6165158, "tests"
assert calculateProblemLevel2(inp_raw, inp, 1) == 17456, "tests"
assert calculateProblemLevel2(inp_raw, inp, 2) == 9158, "tests"
assert calculateProblemLevel2(inp_raw, inp, 3) == 3294746, "tests"


def sumProblems(mat):
    sum_prob = 0
    for i in range(len(mat[0])):
        sum_prob += calculateProblem(mat, i)
    
    return sum_prob


assert sumProblems(mat_test) == 4277556,  "tests"


def sumProblemsLevel2(inp, mat):
    sum_prob = 0
    for i in range(len(mat[0])):
        sum_prob += calculateProblemLevel2(inp, mat, i)
    
    return sum_prob



"""result = sumProblems(inp)
print(result)"""

result2 = sumProblemsLevel2(inp_raw, inp)
print(result2)


# 7090113 trop bas