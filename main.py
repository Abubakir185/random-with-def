import random

def raqamni_top(start, stop):
    random_son = random.randint(start, stop)
    urinishlar_soni = 0
    
    son = int(input(f"{start} va {stop} oraligidagi taxminiy son kiriting: "))
    urinishlar_soni += 1
    

    while son != random_son:
        son = int(input(f"Son kiriting ({start} - {stop}) : "))
         urinishlar_soni += 1
        if son < random_son:
            print("Kiritilgan son kichik.")
        elif son > random_son:
            print("Kiritilgan son katta.")
        elif:
            print("Yutingiz!")
            return urinishlar_soni
           


taxminlar soni = raqamni_top(1, 100)
print(f"Taxminlar soni: {inp_son}"
