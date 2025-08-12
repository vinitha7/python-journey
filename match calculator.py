n1 = int(input("enter a :"))
n2 = int(input("enter b :"))
operator = input("Operator:")

match operator:
    case '+':
        add = n1 + n2
        print(add)
    case '-':
        sub = n1 - n2
        print(sub)
    case '*':
        mul=n1*n2
        print(mul)
    case '/':
        if n2!=0:
            div=n1/n2
            print(div)
        else:
            print("b must be a non-zero")
    case '%':
        per = n1 % n2
        print(per)
    case _:
        print("Please select valid operator")

        