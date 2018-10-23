def caculate (num1, num2):
    result = num1+num2
    print("result = "+ str(result))

def multiplication (num1, num2):
    result = num1 * num2
    print("result = "+ str(result))


def divison (num1, num2):
    result = num1 / num2
    print("result = "+ str(result))


def subtraction (num1, num2):
    result = num1 - num2
    print("result = "+ str(result))


def main():
    print("what operation do you want")
    print("1.Addition\n.2.subtraction\n.3.Mulitiplucation\n.4.division")
    choice = int(input("Enter a number for operation "))
    first = int(input("Enter first number to caculate "))
    second=int(input("Enter second number to caculate "))
    if choice==1:
        addition(first,second)
    elif choice==2:
        subtraction(first,second)
    elif choice==3:
        mulitiplication(first,second)    
    elif choice==4:
        division(first,second)
main()