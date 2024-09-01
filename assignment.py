# 1: calculating discount
def calculate_discount(price, discount_percent):
   if discount_percent >= 20:
        discount = price * discount_percent / 100
        final_price = price - discount
        return final_price
   else:
        return price
   
try:
    price = float(input("Enter the price: "))
    discount_percent = float(input("Enter the discount percentage: "))
    final_price = calculate_discount(price, discount_percent)
    print("The final price is: ", calculate_discount(price, discount_percent))
except ValueError:
    print("Invalid input")
       

      