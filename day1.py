




class Dial:

    def __init__(self):
        self.dial = 50
        self.nb_0 = 0

        with open("input1.txt", "r") as f:
            self.inp = f.read().splitlines()


    def turnNb(self, nb):
        """turns the dial nb times to the right, can be negative and returns the number of times it passed through 0"""

        for _ in range(abs(nb)):
            if nb > 0:
                self.dial += 1
            else:
                self.dial -= 1
            
            self.dial %= 100
                
            self.nb_0 += self.dial == 0


    
    def rotate(self, rotation):
        """makes a rotation, rotation is a str, ex: L18
        also returns the number of times it reached 0 during the rotation"""
        if rotation[0] == "R":
            self.turnNb(int(rotation[1:]))
        else:
            self.turnNb(-int(rotation[1:]))


    def getDial(self):
        """returns the current state of the dial"""
        return self.dial
    

    def getNb_0(self):
        return self.nb_0


    def getInp(self):
        return self.inp


def do_all_rotations(dial: Dial):
    """rotates for each rotation in L and returns the number of times it reached 0"""
    
    for rotation in dial.getInp():
        dial.rotate(rotation)



dial = Dial()

# print(inp)
res = do_all_rotations(dial)
print("result is :", dial.getNb_0())

