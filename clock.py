import datetime

from datetime import date
name = raw_input("Please enter your name: ")
date = raw_input("Enter the date of the gift giving: ")


giftcost = raw_input("Enter How much you want to spent for the Gift: ")
gift = float(giftcost)

shipping = raw_input("Enter Shipping fee if not put zero: ")
ship = float(shipping)

tax = raw_input("Enter the tax amount: ")
t = float(tax)

giftbox = raw_input("Enter how much you want to spend on wrapping the gift: ")
box = float(giftbox)

total_cost = float( gift + ship + t + box )
print "You need to save up $", total_cost


untildate= raw_input("How many days left to the Gift Giving day: ")
udate = float(untildate)
sdate = float(untildate) - 10
print sdate

ddate =  total_cost / sdate

print name ," need to save $",ddate, " everyday until ", date

