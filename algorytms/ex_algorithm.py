class Gen:
    def __init__ (self,genString):
        if genString > 6 : return 0
        self.genString = genString

    def intersectWithArrayOfGens(self, arrayOfGens):
        resultGen = '000000'
        for singleGen in range(6):
            w = 0
            x = 0
            y = 0
            h = 0
            g = 0
            for j in range(len(arrayOfGens)):
                if arrayOfGens[j].genString[singleGen] == 'w':
                    w+= 100
                elif arrayOfGens[j].genString[singleGen] == 'x':
                    x+= 100
                elif arrayOfGens[j].genString[singleGen] == 'y':
                    y+= 60
                elif arrayOfGens[j].genString[singleGen] == 'h':
                    h+= 60
                elif arrayOfGens[j].genString[singleGen] == 'g':
                    g+= 60

                    

