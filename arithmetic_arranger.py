dashes = []
results = []
operand_one = []
operand_two = []
operator = []
output = ""

def arithmetic_arranger(problems, bool=False):
    output = ""
    #deconstructing problems
    for probs in problems:

        deconResult = deconstruct_problem(probs)
        operand_one.append(deconResult[0].strip())
        operand_two.append(deconResult[2].strip())
        operator.append(deconResult[1].strip())

    #validating parameters
      
    #problem length
    if (len(problems) > 5):
        output = "Error: Too many problems."
        return output

    #operator
    for op in operator:
        if (op == '+' or op == '-'):
            continue
        else:
            output = "Error: Operator must be '+' or '-'."
            return output
    #operand one
    for opOne in operand_one:
        if (not (opOne.isdigit())):
            output = "Error: Numbers must only contain digits"
            return output
        elif (int(len(opOne)) > 4):
            output = "Error: Numbers cannot be more than four digits."
            return output

    #operand two
    for opTwo in operand_two:
        if (not (opTwo.isdigit())):
            output = "Error: Numbers must only contain digits"
            return output
        elif (int(len(opTwo)) > 4):
            output = "Error: Numbers cannot be more than four digits."
            return output

    #calculating results
    results = calOperations(operand_one, operator, operand_two)

    #calculating dashes
    for x in range(len(operand_one)):
        dash_count = 0
        if (len(operand_one[x]) > len(operand_two[x])):
            dash_count = int(len(operand_one[x]) + 2)
        elif (len(operand_one[x]) < len(operand_two[x])):
            dash_count = int(len(operand_two[x]) + 2)
        else:
            dash_count = int(len(operand_two[x]) + 2)

        dashes.append(dash_count)

    #adjust raw one

    for x in range(len(operand_one)):
        space_count = dashes[x] - int(len(operand_one[x]))
        if (space_count > 0):
            output = output + (
                (space_count) * " ") + str(operand_one[x]) + "    "
        else:
            output = output + "  " + str(operand_one[x]) + "    "
    output = output + "\n"

    #adjust raw two
    rawTwo = ""
    for x in range(len(operand_two)):
        space_count = dashes[x] - int(len(operand_two[x]))
        if (space_count > 0):
            rawTwo = rawTwo + str(operator[x]) + (
                (space_count - 1) * " ") + str(operand_two[x] + "    ")
        else:
            rawTwo = rawTwo + str(operator[x]) + str(operand_two[x] + "    ")

    output = output + rawTwo + "\n"

    #adjust raw 3

    for x in range(len(dashes)):
        output = output + ((dashes[x]) * "-") + "    "

    #adjust raw 4

    output = output + "\n"
    if (bool):
        for x in range(len(results)):
            space_count = dashes[x] - (len(str(results[x])))
            if (space_count > 0):
                output = output + (int(space_count) * " ") + str(
                    results[x]) + "    "
            else:
                output = output + "  " + str(results[x]) + "    "

    return output


def deconstruct_problem(problem):

    for places in problem:
        if (places == "+"):
            return problem.partition("+")
        elif (places == "-"):
            return problem.partition("-")
        elif (places == "/"):
            return problem.partition("/")
        elif (places == "*"):
            return problem.partition("*")


def calOperations(opOne, operator, opTwo):
    results = []
    for cal in range(len(opOne)):

        if (operator[cal] == "+"):
            results.append((int(opOne[cal]) + int(opTwo[cal])))

        elif (operator[cal] == "-"):
            results.append((int(opOne[cal]) - int(opTwo[cal])))

        elif (operator[cal] == "/"):
            results.append((int(opOne[cal]) / int(opTwo[cal])))

        elif (operator[cal] == "*"):
            results.append((int(opOne[cal]) * int(opTwo[cal])))

    return results
