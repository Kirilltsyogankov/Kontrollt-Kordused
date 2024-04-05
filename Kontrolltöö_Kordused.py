#1
def joonista_kuused(n):
    kuuse_kujutis = ["   /V\\    ",
                     "  / V \\   ",
                     " / V V \\  ",
                     "/VV V VV\\ "]

    for _ in range(n):
        for rida in kuuse_kujutis:
            print(rida)
        print()

#2
def korruta_paaritud_arvud(R):
    tulemus = 1
    for i in range(1, R+1, 2):
        tulemus *= i
    return tulemus

#3
import random

def loe_positiivsed_arvud(N):
    arvud = [random.randint(-100, 100) for _ in range(N)]
    positiivsete_arv = sum(1 for arv in arvud if arv > 0)
    return positiivsete_arv

#4
def loe_paaritud_paaris_arvud(arv):
    paaritu_arv = 0
    paaritu_arv = 0

    for number in str(arv):
        if int(number) % 2 == 0:
            paaritu_arv += 1
        else:
            paaritu_arv += 1
    
    return paaritu_arv, paaritu_arv

#5
def summa_vahemikus(A, B):
    return sum(range(A, B+1))

#6
for _ in range(1, 10):
    joonista_kuused(9)

#7
try:
    R = int(input("Sisesta arv R: "))
    print("Paaritud arvude korrutis vahemikus 0 kuni", R, "on:", korruta_paaritud_arvud(R))
except ValueError:
    print("Viga! Palun sisestage ainult täisarvulisi väärtusi.")

#8
try:
    N = int(input("Sisesta arv N: "))
    print("Positiivsete arvude arv N juhuslike arvude hulgas on:", loe_positiivsed_arvud(N))
except ValueError:
    print("Viga! Palun sisestage ainult täisarvulisi väärtusi.")

#9
try:
    arv = int(input("Sisesta naturaalarv: "))
    paaris_arv, paaritu_arv = loe_paaritud_paaris_arvud(arv)
    print("Paarisarvude arv:", paaris_arv)
    print("Paaritute arvude arv:", paaritu_arv)
except ValueError:
    print("Viga! Palun sisestage ainult täisarvulisi väärtusi.")

#10
try:
    A = int(input("Sisesta väärtus A: "))
    B = int(input("Sisesta väärtus B: "))
    print("Arvude rea summa vahemikus", A, "kuni", B, "on:", summa_vahemikus(A, B))
except ValueError:
    print("Viga! Palun sisestage ainult täisarvulisi väärtusi.")
