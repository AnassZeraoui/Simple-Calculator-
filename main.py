#Creating a Calculator :
#defining functions :
def add(n1,n2):
    return n1 + n2

def substract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2
#defining a Dictionnary :
operations= {
    "+" : add,
    "-" : substract,
    "*" : multiply ,
    "/" : divide
}
def calculate():
    print( """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
""")
    num1 = float(input("What's the first Number ? : "))
    for i in operations.keys():
        print(i)
    should_continue = True
    while should_continue:
        user_operations = input("Which operator are you going to pick from the line above ? : ")
        num2 = float(input("What's the next Number ? : "))
        calcul = operations[user_operations]
        answer = calcul(num1,num2)
        print(f"{num1:.0f}  {user_operations}  {num2:.0f}  = {answer:.1f}")
        yes_no = input("Type 'yes' for re-calculating and 're' for re-starting the calculator : ").lower()
        if yes_no=="yes":
            num1 = answer
        else:
            should_continue = False
            calculate()

calculate()