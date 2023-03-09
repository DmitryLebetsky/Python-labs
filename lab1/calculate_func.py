from constants import OPERATORS_LIST, ADD, SUBTRACT, MULTIPLY, DIVIDE
from helpers import print_calc_result


def calculate(first_operand, second_operand, operator):

    try:
        first_operand = float(first_operand)
        second_operand = float(second_operand)
    except ValueError:
        print("Invalid operands!")
        return

    if operator in OPERATORS_LIST:

        if operator == ADD:
            result = first_operand + second_operand
        elif operator == SUBTRACT:
            result = first_operand - second_operand
        elif operator == MULTIPLY:
            result = first_operand * second_operand
        elif operator == DIVIDE:
            if second_operand == 0:
                print("Dividing by zero!")
                return
            else:
                result = first_operand / second_operand
        else:
            print("Unknown error :(")
            return
        print_calc_result(first_operand, second_operand, operator, result)

    else:
        print("Invalid operator!")
        return


