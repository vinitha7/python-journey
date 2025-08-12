#calculator.py

num1 = int(input("enter a :"))
num2 = int(input("enter b :"))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2

if num2!= 0:
    div = num1 / num2

else:
    print("remainder can't be zero")

print(add,sub,mul,div)