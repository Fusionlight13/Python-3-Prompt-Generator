<h1>Python-3-Prompt-Generator</h1>
    A simple library that easily generates prompts for users to answer questions.

# Example
import PromptDesigner as pb

myQuestion = write_prompt(['Prompt_1', 'Prompt_2', 'Prompt_3'], [['Yes', 'no'], ['ok', 'no'], ['sure', 'nope']], 'String', False)

Parameters: write_prompt([prompt], [choices], [accessType], [exception_handler])

# Explanation:
</h2> Prompt Designer can support multiple questions as long as you have a list per question. The choices however can be as short or as long as you desire in each list. The first parameter, prompt, only needs one list for all the questions. The second parameter, choice, are all the answers a user can choose from for each question. <b>Please note that if you do not have an equal amount of choices for each question, an error will raise and will effectively stop the script from running if it's detected.</b>  </h2> 

# Installation
Download the "PromptDesigner" file and place it into your project directory. It must be added locally into your project because a way has not been found for adding it in globally.

# Changelog 

1.0.0.0
    - Project release</h3>
1.2.0
    -Added in multi question support.


# Backlog

~~- Add functionality for more questions to be asked in one call compared to the usual one.

