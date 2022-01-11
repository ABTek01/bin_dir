#!/usr/bin/env python3
"""
string methods; used to
parse information in large 
strings, sanitize user input
to work in a function, generate
outputs with variable values


string formatting methods; only return new strings,
do not change original string.
"""

"""
string.upper(); #changes all characters to uppercase
string.lower();	#changes all character to lowercase
string.title();	#capitalizes each first character
string.split();	#splits each character or string 
or eliminates a string argument, returns a list of sub-string.
"""

#function that returns the second word of each list element

types_of_eng = 'engineering computers, engineering software, engineering electrical'


split_eng = types_of_eng.split(',') #returns a list from provided argument/string.
def second_word(engineering_type):
    eng_types = []
    for type in engineering_type:
        #splitting each element then appending the last element within the list index.
        eng_types.append(type.split() [-1])
    return eng_types
eng = second_word(split_eng)
print(eng)

#using string.split() to split a string to new lines '\n'

eng_type = """
I am a software engineer and linux systems administrator
by trade. I battle between wanting to focus on frontend
web development and linux operating systems management and
configuration. I think the reason why I tend to switch so 
often is because the work get tedious and I get bored, but
I think it may be symptoms of 'burn out'. I believe I should 
take more breaks
"""

split_str = eng_type.split('\n')
print(split_str)

#joining strings; 'deliminator'.join()
#use 'string_deliminator'.join() on a list.
#'\n'.join(); joins string characters that will be placed on new lines. uses string deliminator.

my_str_list = ['html', 'css,', 'and js', ' are all frontend development programming languages.']
concat_my_str_lst = ' '.join(my_str_list)
a_new_str = 'this is a string too.'
print('+'.join(a_new_str))
print(concat_my_str_lst)


"""
string_var.strip('character'); will get rid of the targetted/argument character 
from the beginning and the end of the string.

string_var.strip(); Stripping a string removes all whitespace 
characters from the beginning and end if no argument is passed in.
""" 
string_var = ' using the .strip() python string method to manipulate strings. '
print(string_var.strip(' '))


"""
.replace(); takes two arguments and replaces all 
instances of the first argument in a string with the second argument. 

*string.replace(character_to_replace, replacer)
"""

linux_string = 'linux, python, automation'
modified_linux_str = linux_string.replace('linux', 'red hat linux')

engineering_string = 'software engineering, ai'
modified_engineering_str = engineering_string.replace('software engineering', 'os engineering')
print(modified_linux_str)
print(modified_engineering_str)




"""
string.find(); finds the index of a string character 
when argument is passed in.
"""
eng_list = []
eng_list.append(modified_linux_str)
eng_list.append(modified_engineering_str)
print(eng_list)

#join the strings of a list
eng_list = ' '.join(eng_list)
print(eng_list)

new_eng_list = []
new_eng_list.append(eng_list)
print(new_eng_list)

"""
.format(); allows us to use
string interpolation, inserting 
values whereever there is a {}.

.format(val1=val1, val2=val2); allows us to
substitute param/arg/values in any order.
"""
eng_message = 'I am a linux {} and {}'
print(eng_message.format('systems administrator', 'software engineer'))

def share_eng_message(linux, software):
    message = 'I code with python as a {software} and configure the {linux} operating system.'
    return message.format(linux=linux, software=software)
eng_message = share_eng_message(software='software engineer', linux='red hat enterprise linux')
print(eng_message)

#splitting list of poems by each comma ','.
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
highlighted_poems_list = highlighted_poems.split(',')

#iterating through list of poems and stripping white space from each indexed poem.
highlighted_poems_stripped = []
for poem in highlighted_poems_list:
    highlighted_poems_stripped.append(poem.strip(' '))
print(highlighted_poems_stripped)

#splitting each poem at the ':'
#appending to empty string
poem_details = []
for i in highlighted_poems_stripped:
    poems_stripped = i.split(':')
    poem_details.append(poems_stripped)
print(poem_details)

#appending details to lists based on their kind.
titles = []
poets = []
dates = []
for i in poem_details:
    titles.append(i[0])
    poets.append(i[1])
    dates.append(i[2])
print(titles, poets, dates)

for l in titles:
    for m in poets:
        for n in dates:
            msg = 'the poem {titles} was published by {poets} in {dates}'.format(titles=titles, poets=poets, dates=dates)
print(msg)

#Thread Shed









    














