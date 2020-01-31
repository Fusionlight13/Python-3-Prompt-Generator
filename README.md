# Python-3-Prompt-Generator
A simple library that easily generates prompts for your user to answer questions. 

# Example
import PromptDesigner as pb

myQuestion = pb.write_prompt('Question here', [list of one type of variable. Strings and ints], True)

Parameters: (question, [list of choices(string or int). Only one type can be used], true/false)

# Explanation:
1. The first parameter is what kind of question you may want to ask
2. The second parameter is a list of choices you want the user to have to answer them. If you have no strings, the choices will become integers. If you have no integers, the choices will be a string. 
3. The third parameter is optional as it's only really useful if your list contains integers. You can make it false for no error handling, but it is recommened to leave on for integers. For strings, not so much.

# Installation
Download the "PromptDesigner" file and place it into your project directory. It must be added locally into your project because a way has not been found for adding it in globally.

# Changelog 1.0.0.0

1.30.20
  - Project release


# Backlog

- Add functionality for more questions to be asked in one call compared to the usual one.

