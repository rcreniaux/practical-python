# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
paid_months = 0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    updated_payement = payment    
    paid_months = paid_months + 1
    if(paid_months >= extra_payment_start_month and paid_months <= extra_payment_end_month):
        updated_payement = payment + extra_payment
    due = principal * (1+rate/12)
    if(due < updated_payement):
        updated_payement = due
    principal = due - updated_payement
    total_paid = total_paid + updated_payement
    print(f'Payment n°{paid_months} : total_paid is {total_paid} and principal is {principal}')

print(f'Total paid is {total_paid} in {paid_months} months')