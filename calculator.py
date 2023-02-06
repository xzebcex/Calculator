# A basic calculator.

class calculator:
    def addition(self):  # Addition.
        print(x + y)

    def subtraction(self):  # Subtraction.
        print(x - y)

    def multiplication(self):  # Multiplication.
        print(x * y)

    def division(self):  # Division.
        print(x / y)


x = int(input('Enter first number: '))

y = int(input('Enter second number: '))

objective = calculator()
choice = 1
while choice != 0:
    print('1 Addition')
    print('2 Subtraction')
    print('3 Multiplication')
    print('4 Division')

    choice = int(input('Enter your choice: '))
    if choice == 1:
        print(objective.addition())
    elif choice == 2:
        print(objective.subtraction())
    elif choice == 3:
        print(objective.multiplication())
    elif choice == 4:
        print(objective.division())
    else:
        print('Invalid choice.')
