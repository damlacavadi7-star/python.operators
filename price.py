original_price = float(input("Ilkin qiymeti daxil et: "))
discount_percent = float(input("Endirim faizini daxil et: "))
discount_amount = original_price * discount_percent / 100
final_price = original_price - discount_amount

print("Ilkin qiymeti daxil et:", original_price)
print("Endirim faizini daxil et:", discount_percent)
print("Endirim meblegi:", discount_amount)
print("Mehsulun endirimden sonraki qiymeti:", final_price)
