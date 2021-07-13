def arithmetic_arranger(list, condition=False):
    if len(list) > 5:
        return "Error: Too many problems."

    first_line = None
    second_line = None
    third_line = None
    fourth_line = None

    for problem in list:
        factors = problem.split()
        if factors[1] != '+' and factors[1] != '-':
            return "Error: Operator must be '+' or '-'."
        elif len(factors[0]) > 4 or len(factors[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        else:
            operator = factors[1]

        try:
            operands = [int(factors[0]), int(factors[2])]
            if factors[1] == '+':
                arranged_problems = operands[0] + operands[1]
            else:
                arranged_problems = operands[0] - operands[1]
        except:
            return "Error: Numbers must only contain digits."

        operands.sort()
        longest_operand = str(operands[1])
        distance = len(operator + ' ' + longest_operand)

        if list[0] == problem:
            first_line = ' '*(distance - len(factors[0])) + factors[0] + ' '*4
            second_line = operator + (' '*(distance - len(operator) - len(factors[2]))) + factors[2] + ' '*4
            third_line = '-'*distance + ' '*4
            fourth_line = (' '*(distance - len(str(arranged_problems)))) + str(arranged_problems) + ' '*4

        elif list[-1] == problem:
            first_line += ' '*(distance - len(factors[0])) + factors[0] + '\n'
            second_line += operator + (' '*(distance - len(operator) - len(factors[2]))) + factors[2] + '\n'

            if condition == True:
                third_line += '-'*distance + '\n'
            else:
                third_line += '-'*distance

            fourth_line += (' '*(distance - len(str(arranged_problems)))) + str(arranged_problems)

        else:
            first_line += ' '*(distance - len(factors[0])) + factors[0] + ' '*4
            second_line += operator + (' '*(distance - len(operator) - len(factors[2]))) + factors[2] + ' '*4
            third_line += '-'*distance + ' '*4
            fourth_line += (' '*(distance - len(str(arranged_problems)))) + str(arranged_problems) + ' '*4

    if (condition == True):
        return (first_line + second_line + third_line + fourth_line)
    else:
        return (first_line + second_line + third_line)

lst = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print (arithmetic_arranger(lst, True))
