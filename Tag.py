class Tag:
    def __init__(self,name,rank):
        self.name = name
        self.rank = rank
    
    def getName(self):
        return self.name

    def getRank(self):
        return self.rank

    def increaseRank(self, int):
        self.rank += int

    def __str__(self):
        return self.name + " " + self.rank.__str__()