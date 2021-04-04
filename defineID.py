class idDefine:
    def __init__(self):
        self.spreadSimplex = 0

        self.genThreshold = 0

        self.toughness = 0
        self.col = [0,0,0]
idDefineList = {}
def getIdDefinitions():
    curID = idDefine()
    curID.spreadSimplex = 10
    curID.genThreshold = 0.2

    curID.toughness = 0.7
    curID.col = [200,100,30]
    idDefineList[1] = curID
    curID = idDefine()
    curID.spreadSimplex = 10
    curID.genThreshold = 0.2
    curID.toughness = 0.7
    curID.col = [100, 100, 30]
    idDefineList[2] = curID
    return idDefineList