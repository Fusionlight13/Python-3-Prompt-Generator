import sys
co = -1
ro = 0
format_arr = []


def write_prompt(prompt, choices, exception_handler):
    global columns
    global rows
    global co
    choiceLimit = len(choices)
    currentChoiceLimit = -1
    for i in range(len(prompt)):
        currentChoiceLimit += 1
        co = -1
        while True:
            try:
                co += 1
                print((choices[currentChoiceLimit][co]))
            except IndexError:
                break


write_prompt(['Question?', 'Are you sure?'], [['Yes', 'no', 'Ok'], ['never', 'sure', 'I guess']], [''])






