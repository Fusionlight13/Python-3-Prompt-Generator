<h1>Python 3 Prompt Generator</h1>
    A simple library that easily generates prompts for users to answer questions.

# Example
<h2>import PromptDesigner as pb</h2>

myQuestion = pb.write_prompt(prompt=['', ''], choices=[['choice_1', 'choice_2',], ['choice_1', 'choice_2']])

# Explanation:
<h2>Prompt Designer can support multiple questions as long as you have a list per question. The choices however can be as short or as long as you desire in each list. The first parameter, prompt, only needs one list for all the questions. The second parameter, choice, are all the answers a user can choose from for each question. <b>Please note that if you do not have an equal amount of choices for each question, an error will raise and will effectively stop the script from running if it's detected.</b></h2> 

# Installation
<h2>Download the "PromptDesigner" file and place it into your project directory. It must be added locally into your project because a way has not been found for adding it in globally.

# Changelog 

1.0.0.0
    - Project release</h3>

1.2.0.0
    - Added in multi question support.


# Backlog

~~- Add functionality for more questions to be asked in one call compared to the usual one.

