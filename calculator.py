def calculator():
    input1 = float(input("Enter your first number: "))
    operation =  input("Enter what do you want to do (+, -, *, /): ")
    input2 = float(input("Enter your second number: "))
    if operation == "+":
        result = input1 + input2
    elif operation == "-":
        result = input1 - input2
    elif operation == "*":
        result = input1 * input2
    elif operation == "/":
        if input2 == 0:
           print("invalid")
        else:
           result = input1 / input2
    else:
        print("invalid operator..")
        print("result: ", result)
calculator()                   