class Matematik:
    def topla(self,sayi1,sayi2):
        return sayi1+sayi2
    def cıkar(self,sayi1,sayi2):
        return sayi1-sayi2
    def carp(self,sayi1,sayi2):
        return sayi1*sayi2
    def bol(self,sayi1,sayi2):
        return sayi1/sayi2
    
matematik=Matematik()
print("bolum :"+str(matematik.bol(5, 4)))