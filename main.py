import random

def raqamni_top(start, stop):
    random_son = random.randint(start, stop)
    urinishlar_soni = 0
    
    son = int(input(f"{start} va {stop} oraligidagi taxminiy son kiriting: "))

    if son < random_son:
        print("Kiritilgan son kichik.")
    elif son > random_son:
        print("Kiritilgan son katta.")
    elif son == random_son:
        print("Yutingiz!")
        print(f"Urinishlar soni {urinishlar_soni}ta")

    if son != random_son:
        urinishlar_soni += 1
    

    while son != random_son:
        
        if son != random_son:
            urinishlar_soni += 1

        son = int(input("Yana urinib koring: "))
        if son < random_son:
            print("Kiritilgan son kichik.")
        elif son > random_son:
            print("Kiritilgan son katta.")
        elif son == random_son:
            print("Yutingiz!")
            print(f"Urinishlar soni {urinishlar_soni}ta")


raqamni_top(1, 100)