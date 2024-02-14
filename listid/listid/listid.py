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

#3
while True:
    try:
        N=int(input("Mitu rida loome? "))
        break
    except:
        print("Vale tüüp")
S=input("Mis sümbol korrutame? ")