calisanlar =["Ahmet","Mehmet","Aslı","Besir"]

fileToAppend=open("Çalışanlar","a")

for calisan in calisanlar:
    fileToAppend.write(calisan)
    fileToAppend.write("\n")


fileToAppend.close()
print(calisanlar)