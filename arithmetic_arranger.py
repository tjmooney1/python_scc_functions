def arithmetic_arranger(problems, display=True):
  # if more than 5 problems to solve, return error message
  if len(problems) > 5:
      return "Error: Too many problems."

  # create objects for the top line, bottom line as well as dash and result
  top_line = ""
  bottom_line = ""
  dash_line = ""
  result_line = ""

  # begin a for loop for every problem in problems object, split into operands with operator between
  for problem in problems:
      operands = problem.split()
      operand1, operator, operand2 = operands

    # if not plus or minus, return an error message
      if operator not in {'+', '-'}:
          return "Error: Operator must be '+' or '-'."

    # if the operands are not digits or numeric, also returmn error
      if not operand1.isdigit() or not operand2.isdigit():
          return "Error: Numbers must only contain digits."

    # define the maximum length of problems by the operands length plus two
      max_length = max(len(operand1), len(operand2)) + 2
      top_line += operand1.rjust(max_length) + "    "
      bottom_line += operator + operand2.rjust(max_length - 1) + "    "
      dash_line += '-' * max_length + "    "

    # create the result and the result line objects for if display = True or False
      result = str(eval(problem))
      result_line += result.rjust(max_length) + "    "

  arranged_problems = top_line.rstrip() + "\n" + bottom_line.rstrip() + "\n" + dash_line.rstrip()

  # if statement for what to do when display = True
  if display:
      arranged_problems += "\n" + result_line.rstrip()

  # return the arranged problems object whether diosplay is True or False
  return arranged_problems
