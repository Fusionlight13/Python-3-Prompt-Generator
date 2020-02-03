import sys


def return_sizes(messages, options):
    number2 = 0
    if type(messages) is list:
        number1 = len(messages)
        for a in options:
            number2 += 1
        return number1, number2
    else:
        return 0, 0


def write_prompt(prompt, choices, access_type ='String', exception_handler=False):
    possible_answers = []
    number_ans = []
    return_vals = []
    current_choice_limit = -1
    incremental_int = 0
    get_input = ''
    size_info = return_sizes(prompt, choices)
    if size_info[0] == 0 and size_info[1] == 0 or size_info[0] is not size_info[1]:
        print('Sizes do not match!')
        sys.exit(1)
    elif size_info[0] == size_info[1]:
        for i in range(len(prompt)):
            current_choice_limit += 1
            co = 0
            while True:
                try:
                    possible_answers.append(choices[current_choice_limit][co])
                    co += 1
                except IndexError:
                    break
            if access_type == 'String':
                full_string = prompt[i]
                for ans in possible_answers:
                    full_string = full_string + str(' | ') + str(ans)
                full_string = full_string + str(': ')
                while get_input not in possible_answers:
                    get_input = input(full_string)
                return_vals.append(get_input)
                possible_answers.clear()
            elif access_type == 'Integer':
                full_string = prompt[i]
                get_input = 0
                for ans in possible_answers:
                    incremental_int += 1
                    full_string = full_string + str(' | ') + str('{}({})'.format(ans, incremental_int))
                    number_ans.append(incremental_int)
                full_string = full_string + str(': ')
                if exception_handler:
                        while get_input not in number_ans:
                            try:
                                get_input = int(input(full_string))
                            except ValueError:
                                print('Value error')
                                get_input = 0
                                continue
                        return_vals.append(get_input)
                        possible_answers.clear()
                        incremental_int = 0
                elif not exception_handler:
                    while get_input not in possible_answers:
                        get_input = input(full_string)
                    return_vals.append(get_input)
                    possible_answers.clear()
                    incremental_int = 0
            else:
                print('Invalid access type!')
        return return_vals


# write_prompt(['Question?', 'Are you sure?'], [['Yes', 'no', 'Ok'], ['never', 'sure', 'I guess']], [''])

answer = write_prompt(prompt=['Question_1', 'Question_2'], choices=[['Yes', 'No'], ['Ok', 'Nope']])
print(answer)



