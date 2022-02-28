

class Jogador():
    def __init__(self, id):
        self.entidades = []
        self.id = id
        self.jaAndou = False
        self.jaAtacou = False
    
    def setEntidades(self,entidades):
        self.entidades.append(entidades)
    
    def setAndou(self):
        self.jaAndou = True
        
    def setAtacou(self):
        self.jaAtacou = True
    
    def getAndou(self):
        return self.jaAndou
    
    def getAtacou(self):
        return self.jaAtacou
    
    
    def resetStatus(self):
        self.jaAtacou = False
        self.jaAndou = False

