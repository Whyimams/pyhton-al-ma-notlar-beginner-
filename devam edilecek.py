class Matematik:
    def __init__(self,a,b):#kesınlıkle 2 tane altre
        self.a = a
        self.b = b
    def topla(self):
        return self.a+self.b
    
    def cikar(self):
        return self.a-self.b
    
    def carp(self):
        return self.a*self.b
    
    def bol(self):
        return self.a/self.b
    
    

matematik2 = Matematik(4,6)
print("Çarpım : "+str(matematik2.carp()))
        