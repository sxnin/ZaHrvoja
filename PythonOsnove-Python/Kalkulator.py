
num1 = float(input("Unesite prvi broj: "))
op = input("Unesite željenu operaciju: ")
num2 = float(input("Unesite drugi broj: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Nije važeća operacija ")
