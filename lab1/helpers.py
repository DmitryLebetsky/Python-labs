from constants import OPERATORS_DICT


def print_calc_result(first_operand, second_operand, operator, result):
    print(str(first_operand) + " " + OPERATORS_DICT[operator] + " " + str(second_operand) + " = " + str(result))