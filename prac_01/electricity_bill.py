TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
# print("Electricity bill estimator")
# cent_per_kwh=float(input("Enter cents per kWh:"))
# daily_use=float(input("Enter daily use in kWh:"))
# days=int(input("Enter number of billing days:"))
# estimated_bill=(cent_per_kwh/100)*days*daily_use
# print(f"Estimated bill ${estimated_bill:.2f}.")
#

print("Electricity bill estimator 2.0")
tariff=int(input("Which tariff? 11 or 31:"))
daily_use=float(input("Enter daily use in kWh:"))
days=int(input("Enter number of billing days:"))
if tariff==31:
    estimated_bill = TARIFF_31* days * daily_use
    print(f"Estimated bill ${estimated_bill:.2f}.")

elif tariff==11:
    estimated_bill=TARIFF_11*days*daily_use
    print(f"Estimated bill ${estimated_bill:.2f}.")

