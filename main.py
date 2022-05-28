import re

def arithmetic_arranger(problems):
  string = ""
  string_2 = ""
  if len(problems) > 5:
    return "Error: Too many problems."
  for problem in problems:
    result = 0
    numbers_array= re.findall('[0-9]+', problem)
    numbers_int = list(map(int, numbers_array))
    qtd_dotted = len(numbers_array[0]) + len(numbers_array[1])
    #dotted = "-"*qtd_dotted
    first_row = " " * (qtd_dotted - len(numbers_array[0]))
    second_row = " "* (qtd_dotted - len(numbers_array[1]))
    if "+" in problem: 
      sum = numbers_int[0] + numbers_int[1]
      result += sum
    if "-" in problem: 
      sub = numbers_int[0] - numbers_int[1]
      result += sub
    else:
      return "Error: Operator must be '+' or '-'."
    first_row_number = first_row + numbers_array[0]
    second_row_number = second_row + numbers_array[1]
    string += first_row_number
    string_2 += second_row_number
    
  string_mae = f"{string}\n{string_2}"
  print(string_mae)
      
