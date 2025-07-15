def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    if n2 != 0:
        return n1/n2
    else:
        return "Error: Division by zero is not allowed"
    
calc_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

while True:
    try:
        n1 = float(input("Type the first number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    while True:
        print("""+
-
*
/
            """)
        op=input("Choose an operator: ")
        if op not in calc_dict:
            print("Invalid operator. Please choose from +, -, *, /")
            continue
        try:
            n2 = float(input("Type the second number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        result= round(calc_dict[op](n1, n2), 2)
        print(f"{n1} {op} {n2} = {result}")
        x=input(f"Type 'y' to continue calculating with {result} or 'n' to start a new calculation or 'q' to quit: ")
        if x=="y":
            n1=result
        elif x=="n":
            break
        else:
            print("Thanks for trying our calculator")
            exit()

        
