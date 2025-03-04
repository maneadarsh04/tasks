# used "def" to define basic calculation.
def Add(num1, num2):
    return num1 + num2
def Subtract(num1, num2):
    return num1 - num2
def Multiply(num1, num2):
    return num1 * num2
def Divide(num1, num2):
    return num1 % num2

print("Please select an operation : \n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

select = int(input("Select operation : "))

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))


if select == 1:
    sum = num1 + num2
    print(f"Addition of {num1} and {num2} is {sum}")

elif select == 2:
     sub = num1 - num2
     print(f"Subtraction of {num1} and {num2} is {sub}")
elif select== 3:
     mulitply = num1 *  num2
     print(f"Multiplication of {num1} and {num2} is {mulitply}")
elif select== 4:
     if (num1>num2):
      divide = float (num1/num2)
     else:
          divide = num2 % num1
     print(f"Division of {num1} and {num2} is {divide}")

