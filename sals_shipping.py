weight = 4

#ground shipping

if weight <= 2:
    msg = str(weight * 1.50 + 20)
    print("Ground shipping cost: $" + msg)
elif ((weight>= 2) and (weight<= 6)):
    msg = str(weight * 3.50 + 20)
    print("Ground shipping cost: $" + msg)
elif ((weight>= 6) and (weight<= 10)):
    msg = str(weight * 4.00 + 20)
    print("Ground shipping cost: $" + msg)
elif weight > 10:
    msg = str( weight * 4.75 + 20)
    print("Ground shipping cost: $" + msg)
else:
    print("error")

ground_shipping_premium = "$125.00"
print("Ground Shipping Premium: " + ground_shipping_premium)

#drone shipping
if weight <= 2:
    msg = (weight * 4.50)
    print("Drone shipping cost: $" + msg)
elif ((weight>=2) and (weight<=6)):
    msg = str(weight * 9.00)
    print("Drone shipping cost: $" + msg)
elif ((weight>= 6) and (weight<=10)):
    msg = str(weight * 12.00)
    print("Drone shipping cost: $" + msg)
elif weight > 10:
    msg = str(weight * 10)
    print("Drone shipping cost: $" + msg)
else:
    print("error")

#