# Wrong Method {Don't do it}
'''age = 50
txt = "My age is " + age
print(txt)'''

#Use format method for concatenation
age = 50
txt = "My age is  {}"
print(txt.format(age))    #My age is  50

#Format Unlimited arguments
qty = 3
itemno  = 567
price = 49.95
myorder = " I want {} pieces of item number {} for price {} Rupees."
print(myorder.format(qty,itemno,price))  # I want 3 pieces of item number 567 for price 49.95 Rupees.

#Format unlimited arguments with indexing

qty = 3
itemno = 567
price =  49.95
myorder = " I want to pay {2} Rupees for {0} pieces of item number {1}."
print(myorder.format(qty,itemno,price))   # I want to pay 49.95 Rupees for 3 pieces of item number 567.