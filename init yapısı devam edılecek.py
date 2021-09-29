class Matematik:
    def ___init___(self,sayi1,sayi2):
        self.sayi1=sayi1
        self.sayi2=sayi2
    def topla(self):
        return self.sayi1+self.sayi2
    def cikar(self):
        return self.sayi1-self.sayi2
    def carp(self):
        return self.sayi1*self.sayi2
    def bol(self):
        return self.sayi1/self.sayi2
matematik=Matematik()
print("Toplam :"+str(matematik.bol(8,5)))
        
