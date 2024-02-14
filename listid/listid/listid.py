#Praktiline iseseisevtöö "Listid"
#1
#from string import *
#vokaali=["a","u","i","o","e","ü","ä","ö","õ"]
#konsonanti="qwrtpsdfghklzxcvbnm"
#märgid=punctuation
#v=k=m=t=0
#tekst=input("Sisesta tekst: ") #"mama"
#print(tekst)
#tekst_list=list(tekst) #["m","a","m","a"]
#print(tekst_list)
#for element in tekst_list:
#    if element.lower() in vokaali:
#        v+=1
#    elif element.lower() in konsonanti:
#        k+=1
#    elif element in märgid:
#        m+=1
#    elif element==" ":
#        t+=1
#print("Vokaali: ",v)
#print("Konsonanti: ",k)
#print("Märgid: ",m)
#print("Tühikud ",t)
#2
#nimed=[]
#for i in range(5):
#    nimi=input("Sisesta nimi: ")
#    nimed.append(nimi)

#print("Sisestatud: ",nimed)
#nimed.sort()
#print("Sorteeritud: ",nimed)
#print("Viimasena oli lisatud: ",nimi)
from random import *
from string import *
#3
#while True:
#    try:
#        N=int(input("Mitu rida loome? "))
#        break
#    except:
#        print("Vale tüüp")
#while True:
#    try:
#        S=input("Mis sümbol korrutame? ")
#        if S in punctuation:
#            break
#        else:
#            print("Vale sümbol")
#    except:
#        print("Vale sümbol")
#for i in range(N):
#    print(randint(1,25)*S)
#4
#Indeksid=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa",
#"Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa",
#"Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
#while True:
#    indeks=input("Indeks: ")
#    if len(indeks)==5 and indeks.isdigit() and indeks[0]!="0": #int(index[0])!=0
#        print("Sa elad piirkonnas",Indeksid[int(indeks[0])-1])
#        if indeks[0]=="1" or indeks[0]=="2" or indeks[0]=="3": #indeks[0] in ["1","2","3"]:
#            print("Kodus")
#        else:
#            print("Maskid")
#        break
#    else:
#        print("Sisesta indeks uuesti: ")
#5
#rida=[]
#N=randint(2,25)
#for i in range(N):
#    rida.append(choice(ascii_uppercase))
#print(rida)
#n=int(input("Mitu paari vahetada "))
#if len(rida)//2>=n:
#    for i in range(n):
#        abi=rida[i]
#        rida[i]=rida[len(rida)-1-i]
#        rida[len(rida)-1-i]=abi
#else:
#    print("Liiga väge elemente")
#print(rida)

#6
#arvud=[1,2,3,4,5,6,122,44,55]
#print(arvud)
#max_=max(arvud)
#indeks=arvud.index(max_)
#max_=int(max_/len(arvud)) #round(max_/len(arvud))
#arvud[indeks]=max_
#print(arvud)

#7
#numbrid = [-10, 5, -3, 8, -1]
#print(numbrid)
#kasvav_nimekiri = sorted(numbrid, key=abs)
#kahanev_nimekiri = sorted(numbrid, key=abs, reverse=True)
#print("Kasvavas järjekorras:", kasvav_nimekiri)
#print("Kahanevas järjekorras:", kahanev_nimekiri)

#12
#import random
#numbrid = [random.randint(1, 100) for _ in range(10)]
#print("Algne loend: ", numbrid)
#min_numb = min(numbrid)
#max_numb = max(numbrid)
#min_indeks = numbrid.index(min_numb)
#max_indeks = numbrid.index(max_numb)
#numbrid[min_indeks], numbrid[max_indeks] = numbrid[max_indeks], numbrid[min_indeks]
#print("Loend pärast vahetust: ", numbrid)

#9
nimi = input("Palun sisestage oma nimi: ")
if nimi.isalpha():
    print(f"Tere, {nimi.capitalize()}!")
    tahtede_arv = len(nimi)
    print(f"Nimes on kokku {tahtede_arv} tähte.")
    vokaalide_arv = sum(1 for taht in nimi if taht.lower() in 'aeiouäöü')
    sugavokaalide_arv = tahtede_arv - vokaalide_arv
    print(f"Nimes on {vokaalide_arv} vokaali ja {sugavokaalide_arv} kaashäälikut.")
    tahtede_list = sorted(set(nimi.lower()))
    print("Tähtede nimekiri tähestikulises järjekorras:")
    print(" ".join(tahtede_list))
else:
    print("Palun sisestage ainult tähti oma nimes.")






