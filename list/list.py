
from random import *
nimed=["Kadri", "Mirje", "Maadis","Kadri", "Kaadri"]
while True:
    v=input("N-andmeta näitamine\nL-andmete lisamine\n").upper()
    if v=="N":
        v=input("Kas kõik?(k) või Juhuslik nimi?(j)").lower()
        if v=="k":
            print(nimed)
        elif v=="j":
            print(choice(nimed))
    elif v=="L":
        v=input("Kas lõppu?(l) või positsioonile?(p)").lower()
        if v=="l":
            nimi=input("Sisesta nimi: ")
            nimed.append(nimi)
        elif v=="p":
            nimi=input("Sisesta nimi: ")
            indeks=int(input("Mis positsioonile: "))
            nimed.insert(indeks-1, nimi)










#sõna="Programmeerimine" #str
#print(sõna)
#loetelu=list(sõna)
#n=len(loetelu)
#print(f" Sõnas {sõna} on {n} tähed")
#print(loetelu)
