def calculator():
    input1 = float(input("Enter your first number: "))
    
    operation =  input("Enter what do you want to do (+, -, *, /): ")
    
    input2 = float(input("Enter your second number: "))
    #operations: 
    if operation == "+":  # add
        result = input1 + input2
    elif operation == "-": #minus
        result = input1 - input2
    elif operation == "*":  #multiply
        result = input1 * input2  
    elif operation == "/": #divide
        if input2 == 0:
           print("invalid")
        else:
           result = input1 / input2 
    else:
        print("invalid operator.. Choose Valid Operator (+, -, *, %)")

    print("result: ", result)
    choice = input("Want to use this again ?")
    if choice == "yes".lower():
        calculator()
    else:
        print("Thanku for using calculator..")
calculator()                 