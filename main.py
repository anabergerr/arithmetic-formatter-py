import re


def arithmetic_arranger(problems):
    string = ""
    for problem in problems:
        dotted = "------"
        value = len(dotted)
        result = 0
        numbers_array = re.findall('[0-9]+', problem)
        numbers_int = list(map(int, numbers_array))
        first_row = " " * (value - len(numbers_array[0]))
        second_row = " " * (value - len(numbers_array[1]))
        if "+" in problem:
            sum = numbers_int[0] + numbers_int[1]
            result += sum
        if "-" in problem:
            sub = numbers_int[0] - numbers_int[1]
            result += sub
        if "*" in problem:
            mult = numbers_int[0] * numbers_int[1]
            result += mult
        if "/" in problem:
            div = numbers_int[0] / numbers_int[1]
            result += div
        first_row_number = first_row + numbers_array[0]
        second_row_number = second_row + numbers_array[1]
        teste = f"{first_row_number}"

        string += teste
    print(string)
