# Basic Functions of a calculator
def add(n1,n2):
    return n1+n2
def subtract (n1,n2):
    return n1-n2
def multiply (n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

    # Creating a dictionary for a calculator

calculator ={
    '+' :add,
    '-': subtract,
    '*' : multiply,
    '/' : divide
}

    # Functionality of a calculator

def cal(x1, x2, operator):
    if operator in calculator:
        x1 = float(x1)
        x2 = float(x2)
        result = calculator[operator](x1,x2)
        print(f'The result is {result}')

        user_choice = input('if you want to continue the transaction type y or type n to cancel it').lower()

        if user_choice == 'y':
            new_value = input("Enter the number")
            new_operator = input("Enter the new Operator you want to calculate")

            cal(result,new_value,new_operator)
        else:
            return result
    else:
        print("Invalid Operator")

x1= input("Enter a number")
x2 = input("Enter number 2")
operator = input("+   -   *   / for your calculation")

final_result = cal(x1,x2,operator)
print(final_result)
