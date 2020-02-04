<h1>Python 3 Prompt Generator</h1>
    A simple library that generates prompts for users

# Example
<h2>import PromptDesigner as pb</h2>

myQuestion = pb.write_prompt(prompt=['', ''], choices=[['choice_1', 'choice_2',], ['choice_1', 'choice_2']])

Keyword types:
 def get_youtube_links(youtube_channel):
        sauce = urllib.request.urlopen(youtube_channel)
        soup = bs.BeautifulSoup(sauce, 'html.parser')
        unformated_channel = []
        s_name = ''
        for url in soup.find_all('a'):
            unformated_channel.append(url.get('href'))
        for item in unformated_channel:
            if '/watch' in item:
                if 'youtube' not in item:
                    s_name = 'https://youtube.com/{}'.format(item)
                    if len(s_name) <= 43:
                        print(s_name)
                else:
                    print(item)




# Keywords explained:


<b>Prompt:</b> Has to be a list. The length can be anywhere between 1 to however much. 
<b>Choices:</b> Must be equal to the questions asked. An infinite amount of choices per question can be used though. No_choices overrides this but must be equal to None.
<b>access_type</b>: String allows you to answer questions as normal with a string according to your choices allowed.
<b>access_type cont'd:</b> Integer allows you to pick a choice corresponding with the int value assigned.
<b>exception_handler:</b> Only useful for ints. Catches value errors. Option automatically set to false and cannot be used when access_type 'String' is on.
<b>no_choices:</b> Lets you answer any question without being restricted to choices available. if access_type is 'String', only string inputs will be allowed.
if access_type is 'Integer', only integer inputs will be allowed. The exception_handler is optional with this mode.

Note: if no choices are needed, use 'choices=None' instead of leaving it empty. Optionally you can use 'choices=[[]]', whichever is easier.
Note: All values are returned into an array with the type of data being dependent on which access_type you selected. Only one type of dataype is currently allowed 


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

~~- Add functionality for several questions to be asked in one call compared to one.

