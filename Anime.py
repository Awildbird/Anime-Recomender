from Tag import Tag

class Anime:
    def __init__(self,english,tags,id):
        self.english = english
        self.tags = []
        self.id = id
        if tags==None:
            self.tags = None
        else:
            for x in tags:
                self.tags.append(Tag(x["name"],x["rank"]))
            
    def getEnglish(self):
        return self.english
    
    def getTags(self):
        return self.tags

    def getId(self):
        return self.id

    def __str__(self):
        if self.tags == None:
            return self.english + " " + self.id.__str__()
        else:
            tagString = ""
            for x in self.tags:
                tagString = tagString + x.__str__() + " "
            return self.english + " " + self.id.__str__() + " " + tagString