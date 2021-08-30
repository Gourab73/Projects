

print('''Welcome!
You need to choose in which form you want to change your number value.''')
print('------------------------------------------------------------------')
print('For Decimal to Binary conversion... press 1.')
print('For Binary to Decimal conversion... press 2.')
print('------------------------------------------------------------------')

numberType = input("Choose the type of the number(1/2): ")

if numberType == '1':

    def decimalToBinary(number1):
        if number1 > 1:
            decimalToBinary(number1 // 2)
        print(number1 % 2,end = '')
        
    def decimalToBinary(number2):
        if number2 > 1:
            decimalToBinary(number2 // 2)
        print(number2 % 2, end = '')

    number1 = int(input("Enter the first positive decimal value: "))
    decimalToBinary(number1)
    print('\n')
    number2 = int(input("Enter the second positive decimal value: "))
    decimalToBinary(number2)


    print('\n')
    print('------------------------------------------------------------------')


    def addition(number1,number2):
        return bin(number1 + number2)

    def subtraction(number1,number2):
        return bin(number1 - number2)

    def multiplication(number1,number2):
        return bin(number1 * number2)

    def division1(number1,number2):
        return bin(number1 % number2)

    def division2(number1,number2):
        return bin(number1 // number2)

    print('''Select the operation you want:
                 1. Addition
                 2. Subtraction
                 3. Multiplication
                 4. Division1(modulus)
                 5. Division2(floor division)''')

    while True:

        Sum = number1 + number2
        Difference = number1 - number2
        Multiply = number1 * number2
        Modulus = number1 % number2
        Floor_Division = number1 // number2
        
        choiceOfOperation = input("Enter your choice of operation(1/2/3/4/5): ")

        print('\n------------------------------------------------------------------')
        

        if choiceOfOperation in ('1','2','3','4','5'):

            if choiceOfOperation == '1':
                print('Addition of the two numbers: ' , addition(number1, number2)) 
            elif choiceOfOperation == '2':
                print('Subtraction of the two numbers: ', subtraction(number1, number2))
            elif choiceOfOperation == '3':
                print('Multiplication of the two numbers: ',  multiplication(number1, number2))
            elif choiceOfOperation == '4':
                print('Modulus of the two numbers: ',  division1(number1, number2))
            elif choiceOfOperation == '5':
                print('Floor Division of the two numbers: ', division2(number1,number2)) 
            break
        else:
            print('Invalid Input')

    if choiceOfOperation == '1':
        print('Decimal of this binary value is: ' + str(Sum))
    elif choiceOfOperation == '2':
        print('Decimal of this binary value is: ' + str(Difference))
    elif choiceOfOperation == '3':
        print('Decimal of this binary value is: ' + str(Multiply))
    elif choiceOfOperation == '4':
        print('Decimal of this binary value is: ' + str(Modulus))
    elif choiceOfOperation == '5':
        print('Decimal of this binary value is: ' + str(Floor_Division))

elif numberType == '2':
    
    def binaryToDecimal(binary): 
        decimal = 0 
        for digit in binary: 
            decimal = decimal*2 + int(digit) 
        print("The decimal value is:", decimal)

    binary = input("Enter a binary number: ")
    binaryToDecimal(binary)


else:
    print('Invalid Input..')
    

              
            
        
