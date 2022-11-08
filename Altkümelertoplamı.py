liste1 = eval(input())
toplam = eval(input())

def add_element(liste):
    binary = []
    altküme = []
    for i in range(2**len(liste)):
        binary.append("{}{}".format((len(liste)-len(bin(i)[2:]))*'0', bin(i)[2:]))
    for k in binary:
        küme = []
        for l in range(len(liste)):   
            if k[l] == "1":
                küme.append(liste[l])
        altküme.append(küme)
    return altküme

def countfind_subset(toplam):
    n = 0
    for t in altliste[1:]:
        if sum(t) == toplam:
            n += 1
    print(n)

altliste = add_element(liste1)
countfind_subset(toplam)