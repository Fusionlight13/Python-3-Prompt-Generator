import sys


def write_prompt(prompt, choices, exception_handler):
    current_answer = ''
    isInt = False
    isString = 0
    isInteger = 0
    valueErrorNeeded = False
    for eachType in choices:
        if type(eachType) == str:
            isString += 1
        elif type(eachType) == int:
            isInteger += 1
    if len(choices) == isString:
        isInt = False
    elif len(choices) == isInteger:
        isInt = True
        if exception_handler:
            valueErrorNeeded = True
    else:
        print('The answers must all be an int or a string!')
        print(len(choices))
        sys.exit(1)
    while current_answer not in choices:
        if isInt:
            if valueErrorNeeded:
                try:
                    for i in range(len(choices)):
                        print('Option {}: {}'.format(i + 1, choices[i]))
                    current_answer = int(input(prompt))

                except ValueError as ex:
                    print(ex)
            else:
                for i in range(len(choices)):
                    print('Option {}: {}'.format(i + 1, choices[i]))
                current_answer = int(input(prompt))
        else:
            for i in range(len(choices)):
                print('Option {}: {}'.format(i + 1, choices))
            current_answer = input(prompt)
    return current_answer


# write_prompt(prompt, [choices], exception_handler, return_val)
# Ex. WritePrompt('How old are you?", [15, 16, 17, 18, 19, 20], True, True