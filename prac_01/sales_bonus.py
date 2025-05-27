"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
BONUS_FOR_UNDER_ONE_THOUSAND=0.1
BONUS_FOR_ONE_THOUSAND_AND_ABOVE=0.15
BONUS_THRESHOLD=1000
sales = float(input("Enter sales: $"))
# if sales>=BONUS_THRESHOLD:
#     user_bonus=sales*BONUS_FOR_ONE_THOUSAND_AND_ABOVE
# else :
#     user_bonus=sales*BONUS_FOR_UNDER_ONE_THOUSAND
# print(user_bonus)

while sales>=0:
    if sales>=BONUS_THRESHOLD:
        bonus=sales*BONUS_FOR_ONE_THOUSAND_AND_ABOVE
    else:
        bonus=sales*BONUS_FOR_UNDER_ONE_THOUSAND
    print(bonus)
    sales = float(input("Enter sales: $"))

