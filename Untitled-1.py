def calculate_total(price_string, quantity_string):
        price = float(price_string) 
        quantity = int(quantity_string)
         
        total = price * quantity
         
        return total 

x = float(input("dose price: "))
y = int(input("dose quantity: "))

total_price = calculate_total(x, y)

print("3.:", total_price)

if total_price > 10:
    print("4.: einai akribo")
else :
    print("4.: einai ftino")    
