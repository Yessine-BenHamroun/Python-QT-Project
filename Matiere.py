class Matiere:
    def __init__(self,code,desi,section,coef,sem):
        self.code = code
        self.desi = desi
        self.section = section
        self.coef = coef
        self.sem = sem
    
    def display(self):
        return "["+self.code+","+self.desi+","+self.section+","+self.coef+","+self.sem+"]"
    