number = int(input("Ikireqemli tam ededi daxil et: "))
tens = number // 10
ones = number % 10
reversed_number = ones * 10 + tens

print("Ikireqemli tam ededi daxil et:", number)
print("Tersine cevrilmis eded:", reversed_number)
