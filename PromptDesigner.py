import sys


def return_sizes(messages, options):
    number1 = 0
    number2 = 0
    if type(messages) is list:
        number1 = len(messages)
        for a in options:
            number2 += 1
        return number1, number2
    else:
        return 0, 0


def write_prompt(prompt, choices, accessType, exception_handler):
    co = 0
    ro = 0
    format_arr = []
    possibleAnswers = []
    number_ans = []
    return_vals = []
    choiceLimit = len(choices)
    currentChoiceLimit = -1
    incremental_int = 0
    get_input = ''
    size_info = return_sizes(prompt, choices)
    if size_info[0] == 0 and size_info[1] == 0 or size_info[0] is not size_info[1]:
        print('Sizes do not match!')
        sys.exit(1)
    elif size_info[0] == size_info[1]:
        for i in range(len(prompt)):
            currentChoiceLimit += 1
            co = 0
            while True:
                try:
                    possibleAnswers.append(choices[currentChoiceLimit][co])
                    co += 1
                except IndexError:
                    break
            if accessType == 'String':
                fullString = prompt[i]
                for ans in possibleAnswers:
                    fullString = fullString + str(' | ') + str(ans)
                fullString = fullString + str(': ')
                while get_input not in possibleAnswers:
                    get_input = input(fullString)
                return_vals.append(get_input)
                possibleAnswers.clear()
            elif accessType == 'Integer':
                fullString = prompt[i]
                get_input = 0
                for ans in possibleAnswers:
                    incremental_int += 1
                    fullString = fullString + str(' | ') + str('{}({})'.format(ans, incremental_int))
                    number_ans.append(incremental_int)
                fullString = fullString + str(': ')
                if exception_handler:
                        while get_input not in number_ans:
                            try:
                                get_input = int(input(fullString))
                            except ValueError:
                                print('Value error')
                                get_input = 0
                                continue
                        return_vals.append(get_input)
                        possibleAnswers.clear()
                        incremental_int = 0
                elif not exception_handler:
                    while get_input not in possibleAnswers:
                        get_input = input(fullString)
                    return_vals.append(get_input)
                    possibleAnswers.clear()
                    incremental_int = 0
            else:
                print('Invalid access type!')
        return return_vals


# write_prompt(['Question?', 'Are you sure?'], [['Yes', 'no', 'Ok'], ['never', 'sure', 'I guess']], [''])





