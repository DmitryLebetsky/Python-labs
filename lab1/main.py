from hello_func import hello_world
from calculate_func import calculate

hello_world()

first_operand = input("Enter first operand: ")
second_operand = input("Enter second operand: ")
operator = input("Enter operand (add, sub, mult, div): ")
calculate(first_operand, second_operand, operator)

