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


def write_prompt(prompt, choices, access_type='String', list_kill=('/k', 4444), exception_handler=False,
                 no_choices=False):
    possible_answers = []
    number_ans = []
    return_vals = []
    current_choice_limit = -1
    incremental_int = 0
    get_input = ''
    if not no_choices:
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
    elif no_choices and access_type == 'String':
        get_input = ''
        for a in prompt:
            get_input = input(a + ' ')
            return_vals.append(get_input)
        return return_vals
    elif no_choices and access_type == 'Integer':
        if not exception_handler:
            get_input = 0
            for l in prompt:
                get_input = int(input(l + ' '))
                return_vals.append(get_input)
            return return_vals
        elif exception_handler:
            get_input = 0
            list_length = len(prompt)
            current_list_length = 0
            while current_list_length is not list_length:
                try:
                    get_input = int(input(prompt[current_list_length] + str(' ')))
                    return_vals.append(get_input)
                    current_list_length += 1
                except ValueError:
                    print('Value error!')
            return return_vals
    elif no_choices and access_type == 'ListStr':
        get_input = ''
        while list_kill[0] not in get_input:
            get_input = input(prompt[0] + ': ')
            return_vals.append(get_input)
        if list_kill[0] in return_vals:
            return_vals.remove(list_kill[0])
        return return_vals
    elif no_choices and access_type == 'ListInt':
        get_input = 0
        if exception_handler:
            while list_kill[1] != get_input:
                try:
                    get_input = int(input(prompt[0] + ': '))
                    return_vals.append(get_input)
                except ValueError:
                    print('Value error!')
                if list_kill[1] in return_vals:
                    return_vals.remove(list_kill[1])
                return return_vals
        elif not exception_handler:
            while list_kill[1] != get_input:
                get_input = int(input(prompt[0] + ': '))
                return_vals.append(get_input)
            if list_kill[1] in return_vals:
                return_vals.remove(list_kill[1])
            return return_vals


# write_prompt(['Question?', 'Are you sure?'], [['Yes', 'no', 'Ok'], ['never', 'sure', 'I guess']], [''])
if __name__ == '__main__':
    fav_songs = write_prompt(prompt=['What is your favorite songs?'],
                             choices=None, access_type='ListInt', no_choices=True)
    print(fav_songs)



