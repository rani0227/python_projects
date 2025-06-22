def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
operations_dic={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    a=float(input("Enter first number :"))
    for i in operations_dic:
        print(i)
    continue_flag=True
    while continue_flag:    
        op_symbol=input("Pick an operation :")
        b=float(input("Enter second number :"))  
        calculator_function=operations_dic[op_symbol] 
        output=calculator_function(a,b)
        print(f"{a} {op_symbol} {b} = {output}") 
        should_continue=input(f"enter 'y' to continue calculation with {output} or 'n' to start a new calculation or 'x' to exit :").lower()
        if should_continue=='y':
            a=output
        elif should_continue=='n':
            continue_flag=False
            calculator()
        else:
            continue_flag=False
            print("Bye")  
calculator()              
