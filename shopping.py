price = float(input("Mehsulun qiymeti: "))
quantity = int(input("Mehsulun sayi: "))
money = float(input("Verdiyin pul: "))

total = price * quantity
change = money - total

print("Umumi qiymet:", total)
print("Qalan pul:", change)
