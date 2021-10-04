f = open("Müsteriler.txt")

#print(f.read())#eğer bunu yazdıktan sonra readline eklersek okumaz çünkü bu komutta her şeyi okumuş olacaktır 
print("**********")

#dosya satırlarını tamamını tek tek gezip yazdırır
for l in f:
    print(l)



