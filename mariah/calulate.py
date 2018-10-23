def calculate(num1, num2):

    result= num1 + num2

    print("result = " + str(result))



def multiplication(num1, num2):

    result= num1 * num2

    print("result = " + str(result))



def subtraction(num1, num2):

    result= num1 - num2

    print("result = " + str(result))



def division(num1, num2):

    result= num1 / num2

    print("result = " + str(result))



def main():
    print("what operation do want to do?\n 1.Addition \n 2. subtraction \n3. Multiplication \n 4. Division\n")
    choice=int(input("Enter number of operation"))
    first=int(input("Enter first number to calulate"))
    second=int(input("Enter second number to calulate"))
    if choice=='1':
        addition(first,second)
    elif choice==2:
        subtraction(first,second)
    elif choice==3:
        multiplication(first,second)
    elif choice==4:
        divison(first,second)

main()
               
