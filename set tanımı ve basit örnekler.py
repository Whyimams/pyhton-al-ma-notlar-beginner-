studentSet = {"Ahmet","Derin","Sevde","zeynep"}
print(studentSet)  #belirli bir sıralamaya göre yazmayacaktır!!

if "Derin" in studentSet :
    print("listede var")
else :
    print("listede yok")
    
studentSet.add("Ali")
print(studentSet)
studentSet.update(["eren","emre"])
print(studentSet)
studentSet.pop()
print(studentSet)