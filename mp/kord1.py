#3variant

#1

#n=int(input("Введите число от 1 до 9: "))
#if 0<n<10:
#    for i in range(n):
#        print("  -----",end="")
#    print()
#    for i in range(n):
#        print("|  O  |", end="")
#    print()
#    for i in range(n):
#        print("! -- !", end="")
#    print()
#    for i in range(n):
#        print("  -----", end="")
#    print()
#else:
#    print("Некорректный ввод. Введите число от 1 до 9.")

#2

#try:
#    power = int(input("Введите показатель степени: "))
#    n = float(input("Введите число n: "))

#    i = 0
#    while True:
#        result = n**i
#        if result <= n**3:
#            print(f"{n} в степени {i} равно {result}")
#            i=i+1
#        else:
#            break

#except ValueError:
#    print("Ошибка: Введите корректные значения.")
#except Exception as e:
#    print(f"ошибка: {e}")
#3

#õpilasi_kokku=10
#hinded_kokku=0
#while True:
#    try:
#        for i in range(õpilasi_kokku):
#            hinne=float(input(f"Введите оценку ученика {i+1}: "))
#            hinded_kokku+=hinne
#    except ValueError:
#        print("Ошибка.")
#        continue
#    else:
#        break
#keskmine_hinne=hinded_kokku/õpilasi_kokku
#print(f"Средняя оценка по физике: {keskmine_hinne}")
#4
#kingitus=0
#vanus=1
#while kingitus <=100:
#    kingitus+=vanus
#    vanus+=1
#print("Подарок превысит 100$ на", vanus-1, "день рождения.")
#5
a, b = 0, 1
print(a, b, end="")
for i in range(7):
    a, b = b, a + b
    print(b, end="")
