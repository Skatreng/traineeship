#Калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

#Поддерживаемые операции: +, -, /, *, mod, pow, div, где
#mod — это взятие остатка от деления,
#pow — возведение в степень,
#div — целочисленное деление.

#Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

divisionByZeroMessage = "Деление на 0!"
firstOperand = float(input())
secondOperand = float(input())
operator = input()

if operator == "+":
    print(firstOperand + secondOperand)
elif operator == "-":
    print(firstOperand - secondOperand)
elif operator == "/":
    if secondOperand == 0:
        print(divisionByZeroMessage)
    else:
        print(firstOperand / secondOperand)
elif operator == "*":
    print(firstOperand * secondOperand)
elif operator == "mod":
    if secondOperand == 0:
        print(divisionByZeroMessage)
    else:
        print(firstOperand % secondOperand)
elif operator == "div":
    if secondOperand == 0:
        print(divisionByZeroMessage)
    else:
        print(firstOperand // secondOperand)
elif operator == "pow":
    print(firstOperand ** secondOperand)


