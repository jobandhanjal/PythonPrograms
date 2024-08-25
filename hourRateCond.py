hour = float(input('Please enter hours :'))
hour_rate = float(input('Please enter hours rate :'))
gross_pay = 0.0
if hour > 40.0 :
    gross_pay = ((hour - 40) * hour_rate * 1.5) + ( 40 * hour_rate )
else: 
    gross_pay = ( hour * hour_rate )
print(f'Your Gross Pay : {gross_pay}')