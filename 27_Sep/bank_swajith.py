#1
total_amount=int(input("principle"))
i=int(input("rate of interest"))
m5=int(input("amount withdrawn"))
m9=int(input("amount added"))
intrest_upto_5months=(total_amount*4/12*i)/100;
intrest_upto_9months=((total_amount-m5)*4/12*i)/100;
remaining_months=((total_amount-m5+m9)*4/12*i)/100;
print((total_amount-m5+m9)+intrest_upto_5months+intrest_upto_9months+remaining_months)
#2
p=int(input())
I1=(p*(4/12)*12)/100
p=p-25000
I2=(p*(4/12)*12)/100
p=p+10000
I3=(p*(4/12)*12)/100
p=p+I1+I2+I3
print("balance",p)
#memory address
a=100
print(id(a))
a=100
print(id(a))
a="abc"
print(id(a))
b=100
print(id(b))

#values same, variables different, memory address immutable
#variables same,different values, memory address mutable

