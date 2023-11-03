class Notes:
    def __init__(self,num,code,ds,ex):
        self.num = num
        self.code=code
        self.ds = ds
        self.ex = ex
    
    def display(self):
        return "["+self.num+","+self.code+","+self.ds+","+self.ex+"]"