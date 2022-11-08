class person:
    def __init__(self,name,lastname,age):
        self.name=name
        self.lastname=lastname
        self.age=age
        
person1=person("Beşir","Alkaya","22")


class worker(person):
    def __init__(self,salary):
        self.salary=salary
        
class customer(person):
    def __init__(self,creditcardnumber):
        self.creditcardnumber=creditcardnumber



mehmet=customer(1323232)
print(mehmet.creditcardnumber)

