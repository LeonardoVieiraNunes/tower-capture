
class Casa:
    def __init__(self,id,casaConfig):
        self.id = id
        self.entidade = None
    
    def getEntidade(self):
        return self.entidade
    
    def setEntidade(self,entidade):
        self.entidade = entidade