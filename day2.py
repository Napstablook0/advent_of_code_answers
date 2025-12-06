


def isIdValidLevel1(id: str):
    """returns True if the id is valid, False otherwise"""
    assert type(id) == str, "id must be str"

    n = len(id)

    
    if n % 2 != 0:
        return True
    
    return id[:n//2] != id[n//2:]

    
def isIdValidLevel2(id: str):
    n =  len(id)

    for i in range(1, n):
        if n % i == 0:
            j = 0
            pattern_found = True
            while j < n//i - 1 and pattern_found:

                if id[j*i:(j+1)*i] != id[(j+1)*i:(j+2)*i]:
                    pattern_found = False
                j += 1
            
            if pattern_found:
                return False
            
    return True



# TESTS FOR LEVEL 1

id1 = "3"
assert isIdValidLevel1(id1) == True, "test isIdValidLevel1"
id2 = "11"
assert isIdValidLevel1(id2) == False, "test isIdValidLevel1"
id3 = "111"
assert isIdValidLevel1(id3) == True, "test isIdValidLevel1"
id4 = "1212"
assert isIdValidLevel1(id4) == False, "test isIdValidLevel1"
id5 = "123123"
assert isIdValidLevel1(id5) == False, "test isIdValidLevel1"
id6 = "123423"
assert isIdValidLevel1(id6) == True, "test isIdValidLevel1"
id7 = "123124"
assert isIdValidLevel1(id7) == True, "test isIdValidLevel1"
id8 = "423123"
assert isIdValidLevel1(id8) == True, "test isIdValidLevel1"

id2 = "12"
assert isIdValidLevel1(id2) == True, "test isIdValidLevel1"
id3 = "121"
assert isIdValidLevel1(id3) == True, "test isIdValidLevel1"
id4 = "1242"
assert isIdValidLevel1(id4) == True, "test isIdValidLevel1"
id5 = "423123"
assert isIdValidLevel1(id5) == True, "test isIdValidLevel1"
id6 = "123423"
assert isIdValidLevel1(id6) == True, "test isIdValidLevel1"
id7 = "123124"
assert isIdValidLevel1(id7) == True, "test isIdValidLevel1"
id8 = "423123"
assert isIdValidLevel1(id8) == True, "test isIdValidLevel1"



# TESTS FOR LEVEL 2

id1 = "3"
assert isIdValidLevel2(id1) == True, "test isIdValidLevel2"
id2 = "11"
assert isIdValidLevel2(id2) == False, "test isIdValidLevel2"
id3 = "111"
assert isIdValidLevel2(id3) == False, "test isIdValidLevel2"
id4 = "1212"
assert isIdValidLevel2(id4) == False, "test isIdValidLevel2"
id5 = "123123"
assert isIdValidLevel2(id5) == False, "test isIdValidLevel2"
id6 = "123423"
assert isIdValidLevel2(id6) == True, "test isIdValidLevel2"
id7 = "123124"
assert isIdValidLevel2(id7) == True, "test isIdValidLevel2"
id8 = "423123"
assert isIdValidLevel2(id8) == True, "test isIdValidLevel2"

id2 = "12"
assert isIdValidLevel2(id2) == True, "test isIdValidLevel2"
id3 = "121"
assert isIdValidLevel2(id3) == True, "test isIdValidLevel2"
id4 = "1242"
assert isIdValidLevel2(id4) == True, "test isIdValidLevel2"
id5 = "423123"
assert isIdValidLevel2(id5) == True, "test isIdValidLevel2"
id6 = "123423"
assert isIdValidLevel2(id6) == True, "test isIdValidLevel2"
id7 = "123124"
assert isIdValidLevel2(id7) == True, "test isIdValidLevel2"
id8 = "423123"
assert isIdValidLevel2(id8) == True, "test isIdValidLevel2"
id9 = "121212"
assert isIdValidLevel2(id9) == False, "test isIdValidLevel2"
id10 = "121213"
assert isIdValidLevel2(id10) == True, "test isIdValidLevel2"
id11 = "321212"
assert isIdValidLevel2(id11) == True, "test isIdValidLevel2"




with open("input2.txt", "r") as f:
    inp = list(f.read())



def convertInpToList(inp):
    """ids will be str"""
    L = []
    mini = ""
    maxi = ""
    currently_doing_mini = True
    for caracter in inp:
        if caracter == "-":
            currently_doing_mini = False
        elif caracter == ",":
            for i in range(int(mini), int(maxi)+1):
                L.append(str(i))
            mini = ""
            maxi = ""
            currently_doing_mini =  True
        else:
            if currently_doing_mini:
                mini += caracter
            else:
                maxi += caracter
    
    for i in range(int(mini), int(maxi)+1):
        L.append(str(i))
    
    return L


def getAllInvalidIdsLevel1(id_list):
    """also converts ids to int"""
    L = []
    for id in id_list:
        if not isIdValidLevel1(id):
            L.append(int(id))
    
    return L


def getAllInvalidIdsLevel2(id_list):
    """also converts ids to int"""
    L = []
    for id in id_list:
        if not isIdValidLevel2(id):
            L.append(int(id))
    
    return L




inp_id_list = convertInpToList(inp)
valid_ids_level1 = getAllInvalidIdsLevel1(inp_id_list)
valid_ids_level2 = getAllInvalidIdsLevel2(inp_id_list)

print("level 1 answer :", sum(valid_ids_level1))
print("level 2 answer :", sum(valid_ids_level2))
