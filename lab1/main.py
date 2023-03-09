from hello_func import hello_world
from calculate_func import calculate
from create_odd_list import create_odd_list

hello_world()

print()
first_operand = input("Enter first operand: ")
second_operand = input("Enter second operand: ")
operator = input("Enter operand (add, sub, mult, div): ")
calculate(first_operand, second_operand, operator)

print()
print("Create your list of integer values. Press enter to stop filling it")
odd_list = create_odd_list()
print("Odd list: " + str(odd_list))

