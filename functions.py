def calculate_discount(price, discount_percent):

    if discount_percent >=20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
def main():
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    final_price = calculate_discount(price, discount_percent) 

    if discount_percent >=20:
        print(f"A discount of {discount_percent}% has been applied.")
    else:
        print(f"No dicount applied. The discount percentage must be 20% or higher.")

    print(f"The final price is: ${final_price:.2f}")

    







