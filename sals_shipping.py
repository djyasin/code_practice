weight = 41.5

#ground shipping

if weight <= 2:
  print(weight * 1.50 + 20)
elif ((weight>= 2) and (weight<= 6)):
  print (weight * 3.50 + 20)
elif ((weight>= 6) and (weight<= 10)):
  print(weight * 4.00 + 20)
elif weight > 10:
  print( weight * 4.75 + 20)
else:
  print("error")

ground_shipping_premium = "$125.00"
print("Ground Shipping Premium: " + ground_shipping_premium)

#drone shipping
if weight <= 2:
   print(weight * 4.50)
elif ((weight>=2) and (weight<=6)):
  print(weight * 9.00)
elif ((weight>= 6) and (weight<=10)):
  print(weight * 12.00)
elif weight > 10:
  print(weight * 10)
else:
  print("error")

#