total=0
discount_threshold=100
discount_percentage=0.10
number_of_items=int(input("Number of items?"))
while number_of_items<=0:
    print("Invalid input!")
    number_of_items = int(input("Number of items?"))

for i in range(1,number_of_items+1):
    price=float(input("Price of item:"))
    total+=price

if total>discount_threshold:
    discount=total*discount_percentage
    total=total-discount
print(f"Total for {number_of_items} is ${total}.")