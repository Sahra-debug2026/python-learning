price= int(input("give me the price:"))

if price > 100 :
    discont = 0.2* price

else:
    discount = 0.1* price
final_price = price - discont    
print(f"your discont is {discont} and you need to pay = {final_price}.")   


