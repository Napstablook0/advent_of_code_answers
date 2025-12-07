"""le level 2 ne marche pas"""

def findFirstGreatestBattery(bank: str) -> tuple[str, int]:
    """finds and returns the first battery that will be turned on"""
    assert type(bank) == str, "bank must be str"
    assert bank != "", "bank must be non empty string"

    n = len(bank)
    maximum_battery = "0"
    index_battery = 0
    for i in range(n-1):
        battery = bank[i]
        if int(battery) > int(maximum_battery):
            maximum_battery = battery
            index_battery = i

    return maximum_battery, index_battery



# testing the function
assert findFirstGreatestBattery("987654321111111") == ("9", 0), "tests"
assert findFirstGreatestBattery("811111111111119") == ("8", 0), "tests"
assert findFirstGreatestBattery("234234234234278") == ("7", 13), "tests"
assert findFirstGreatestBattery("818181911112111") == ("9", 6), "tests"




def findBatteries(bank):
    assert type(bank) == str, "bank must be str"
    assert bank != "", "bank must be non empty string"

    
    first_battery, index_first_battery = findFirstGreatestBattery(bank)

    second_battery_range = bank[index_first_battery+1:] + "0"
    second_battery, index_second_battery = findFirstGreatestBattery(second_battery_range)

    return first_battery + second_battery



# testing the function
assert findBatteries("987654321111111") == "98", "tests"
assert findBatteries("811111111111119") == "89", "tests"
assert findBatteries("234234234234278") == "78", "tests"
assert findBatteries("818181911112111") == "92", "tests"
assert findBatteries("91") == "91", "tests"
assert findBatteries("1423") == "43", "tests"
assert findBatteries("612345") == "65", "tests"



def removeFirstLowestBattery(bank) -> str:
    assert type(bank) == str, "bank must be str"
    assert bank != "", "bank must be non empty string"

    n = len(bank)
    minimum = 10
    index_minimum = None

    for i in range(n):
        battery = bank[i]

        if int(battery) < minimum:
            minimum = int(battery)
            index_minimum = i

    
    return bank[:index_minimum] + bank[index_minimum+1:]


assert removeFirstLowestBattery("987654321111111") == "98765432111111", "tests"
assert removeFirstLowestBattery("811111111111119") == "81111111111119", "tests"
assert removeFirstLowestBattery("234234234234278") == "34234234234278", "tests"
assert removeFirstLowestBattery("818181911112111") == "88181911112111", "tests"
assert removeFirstLowestBattery("8181819111211") == "881819111211", "tests"
assert removeFirstLowestBattery("76598889") == "7698889", "tests"
assert removeFirstLowestBattery("176598889") == "76598889", "tests"
assert removeFirstLowestBattery("3533343533443433343344434533332") == "353334353344343334334443453333", "tests"






def getAllBanks():
    with open("input3.txt", "r") as f:
        inp  = f.read().splitlines()

    return inp


def findAllGreatestJoltages(batteries: list[str]):
    assert type(batteries) == list, "batteries must be a list of batteries (str)"
    for battery in batteries:
        assert type(battery) == str, "batteries must be a list of batteries (str)"

    joltages = []
    for battery in batteries:
        best_joltage = findBatteries(battery)
        joltages.append(int(best_joltage))
    
    return joltages


# testing the function
assert findAllGreatestJoltages(["987654321111111", "811111111111119"]) == [98, 89], "tests"
assert findAllGreatestJoltages(["811111111111119", "234234234234278"]) == [89, 78], "tests"
assert findAllGreatestJoltages(["91", "91"]) == [91, 91], "tests"
assert findAllGreatestJoltages(["612345", "811111111111119"]) == [65, 89], "tests"





inp = getAllBanks()
joltages_level1 = findAllGreatestJoltages(inp)
result = sum(joltages_level1)
print("result level 1 :", result)

