def arithmetic_arranger(problems, display=True):
  if len(problems) > 5:
      return "Error: Too many problems."

  top_line = ""
  bottom_line = ""
  dash_line = ""
  result_line = ""

  for problem in problems:
      operands = problem.split()
      operand1, operator, operand2 = operands

      if operator not in {'+', '-'}:
          return "Error: Operator must be '+' or '-'."

      if not operand1.isdigit() or not operand2.isdigit():
          return "Error: Numbers must only contain digits."

      max_length = max(len(operand1), len(operand2)) + 2
      top_line += operand1.rjust(max_length) + "    "
      bottom_line += operator + operand2.rjust(max_length - 1) + "    "
      dash_line += '-' * max_length + "    "

      result = str(eval(problem))
      result_line += result.rjust(max_length) + "    "

  arranged_problems = top_line.rstrip() + "\n" + bottom_line.rstrip() + "\n" + dash_line.rstrip()

  if display:
      arranged_problems += "\n" + result_line.rstrip()

  return arranged_problems
