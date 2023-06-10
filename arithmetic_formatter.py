def arithmetic_arranger(problems, solve=False):

  # problems is an array of strings
  # separate strings to be separately evaluated
  words = []
  firstNum = []
  oper = []
  secondNum = []
  solution = []
  firstLine = []
  secondLine = []
  thirdLine = []
  fourthLine = []

  if len(problems) > 5:
    return "Error: Too many problems."

  for problem in problems:

    # separate problem into nums + operator
    words = problem.split()
    try:
      firstNum.append(int(words[0]))
    except:
      return "Error: Numbers must only contain digits."
    oper.append(words[1])
    try:
      secondNum.append(int(words[2]))
    except:
      return "Error: Numbers must only contain digits."

    # calculate solution
    if oper[-1] == '+':
      solution.append(firstNum[-1] + secondNum[-1])
    elif oper[-1] == '-':
      solution.append(firstNum[-1] - secondNum[-1])
    else:
      return "Error: Operator must be '+' or '-'."

    # right-align nums
    secondLine.append(oper[-1])

    #determine size of longest line in problem, set all to fit in that size
    if len(str(firstNum[-1])) > len(str(secondNum[-1])):
      size = len(str(firstNum[-1])) + 2
    else:
      size = len(str(secondNum[-1])) + 2
    if (size >= 7):
      return "Error: Numbers cannot be more than four digits."

    # set number of spaces before firstNum
    i = 0
    while i < size - len(str(firstNum[-1])):
      firstLine.append(' ')
      i += 1
    # set number of spaces between oper and secondNum
    i = 0
    while i < size - (len(str(secondNum[-1])) + 1):
      secondLine.append(' ')
      i += 1
    # set number of '-' on thirdLine
    i = 0
    while i < size:
      thirdLine.append('-')
      i += 1
    # set number of spaces before solution
    if (solve == True):
      i = 0
      while i < size - len(str(solution[-1])):
        fourthLine.append(' ')
        i += 1

    #arrange numbers onto lines
    firstLine.append(str(firstNum[-1]))
    secondLine.append(str(secondNum[-1]))
    if (solve == True):
      fourthLine.append(str(solution[-1]))

    # create 4 ' ' chars on each line to separate problems
    i = 0
    while i < 4:
      firstLine.append(' ')
      secondLine.append(' ')
      thirdLine.append(' ')
      if (solve == True):
        fourthLine.append(' ')
      i += 1

  # turn lines into strings, remove whitespace after last problem
  arranged_problems = []
  arranged_problems.append((''.join(firstLine)).rstrip())
  arranged_problems.append('\n')
  arranged_problems.append((''.join(secondLine)).rstrip())
  arranged_problems.append('\n')
  arranged_problems.append((''.join(thirdLine)).rstrip())
  if solve == True:
    arranged_problems.append('\n')
    arranged_problems.append((''.join(fourthLine)).rstrip())

  arranged_problems = "".join(arranged_problems)

  return arranged_problems


def main():
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))

if __name__ == "__main__":
    main()