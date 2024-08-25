hour = int(input('Please enter hours :'))
hour_rate = int(input('Please enter hours rate :'))
def computePay(hour,hour_rate) :
    if hour > 40.0 :
        gross_pay = ((hour - 40) * hour_rate * 1.5) + ( 40 * hour_rate )
    else:
        gross_pay = ( hour * hour_rate )
    return gross_pay
value = computePay(hour,hour_rate)
print(f'Gross Pay is : {value}')