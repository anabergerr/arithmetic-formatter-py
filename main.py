import re


def verify_errors(element):
    split_problem = element.split()
    len_item_one = len(split_problem[0])
    len_item_two = len(split_problem[2])
    if len_item_one > 4 or len_item_two > 4:
        return 'Error: Numbers cannot be more than four digits.'
    if not split_problem[0].isdigit() or not split_problem[2].isdigit():
        return "Error: Numbers must only contain digits."
    if element == "*" or element == "/":
        return "Error: Operator must be '+' or '-'."


def arithmetic_arranger(problems):
    string = ""
    string_two = ""

    for problem in problems:
        result = 0
        errors = verify_errors(problem)
        if errors:
            return errors
        numbers_array = re.findall('[0-9]+', problem)
        numbers_int = list(map(int, numbers_array))
        qtd_dotted = len(numbers_array[0]) + len(numbers_array[1])
        #dotted = "-"*qtd_dotted
        first_row = " " * (qtd_dotted - len(numbers_array[0]))
        second_row = " " * (qtd_dotted - len(numbers_array[1]))
        if "+" in problem:
            sum = numbers_int[0] + numbers_int[1]
            result += sum
        if "-" in problem:
            sub = numbers_int[0] - numbers_int[1]
            result += sub
        first_row_number = first_row + numbers_array[0]
        second_row_number = second_row + numbers_array[1]
        string += first_row_number
        string_two += second_row_number


print(arithmetic_arranger(["32g + 698", "3801 - 2", "45 + 43", "123 + 49"]))
