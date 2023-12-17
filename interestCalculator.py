# colllect the neccary inputs principal apr , years ,


print("This is a monthly payment loan Calculator")
print("")

principal = float(input("Input the laon amount : "))
apr = float(input("Input the annual interset rate: "))
years =int(input("input amount of years : "))


monthly_interest_rate  = apr/1200
amount_0f_months = years*12
monthly_payment = principal*monthly_interest_rate/(1-(1+monthly_interest_rate)**(-amount_0f_months ))
print("Monthly payment for this loan is : ",monthly_payment)