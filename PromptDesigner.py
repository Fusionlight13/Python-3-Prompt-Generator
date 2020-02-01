import sys
co = 0
ro = 0
format_arr = []


def return_sizes(messages, options):
    number1 = 0
    number2 = 0
    if type(messages) is list:
        number1 = len(messages)
        for a in options:
            number2 += 1
        return number1, number1
    else:
        return 0, 0


def write_prompt(prompt, choices, exception_handler):
    global columns
    global rows
    global co
    choiceLimit = len(choices)
    currentChoiceLimit = -1
    size_info = return_sizes(prompt, choices)
    if size_info[0] == 0 and size_info[1] == 0:
        print('Sizes do not match!')
        sys.exit(1)
    elif size_info[0] == size_info[1]:
        for i in range(len(prompt)):
            currentChoiceLimit += 1
            co = 0
            while True:
                try:
                    print((choices[currentChoiceLimit][co]))
                    co += 1
                except IndexError:
                    break

            print(prompt[i])

            currentChoiceLimit = -1


# write_prompt(['Question?', 'Are you sure?'], [['Yes', 'no', 'Ok'], ['never', 'sure', 'I guess']], [''])
write_prompt(['Question', 'Yes'], [['one', 'two']], True)





