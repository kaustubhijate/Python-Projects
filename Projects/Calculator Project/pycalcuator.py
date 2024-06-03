# Calculator.
from art import logo;
def add(n1,n2):
    return n1 + n2;

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2;

def divide(n1,n2):
    return n1/n2;

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():

    print(logo);

    num1 = float(input("Enter the first number: "));
    for symbol in operations:
        print(symbol);

    should_continue = True;

    while should_continue:

        operation_symbol = input("pick the operation symbol: ");
        num2 = float(input("Enter the next number: "));

        calculate_function = operations[operation_symbol]
        answer = calculate_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer} ")
        if input(f"To continue the operation type {"y"} or to exit type {"n"}: ") == "y":
            num1=answer
        else:
            should_continue = False;
            calculator();


calculator();
