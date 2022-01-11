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
#string layout customer, price, color, date
daily_sales = \
"""Edith Mcbride   ;,;$1.21   ;,;   white ;,; 
09/15/17   ,Herbert Tran   ;,;   $7.29;,; 
white&blue;,;   09/15/17 ,Paul Clarke ;,;$12.52 
;,;   white&blue ;,; 09/15/17 ,Lucille Caldwell   
;,;   $5.13   ;,; white   ;,; 09/15/17,
Eduardo George   ;,;$20.39;,; white&yellow 
;,;09/15/17   ,   Danny Mclaughlin;,;$30.82;,;   
purple ;,;09/15/17 ,Stacy Vargas;,; $1.85   ;,; 
purple&yellow ;,;09/15/17,   Shaun Brock;,; 
$17.98;,;purple&yellow ;,; 09/15/17 , 
Erick Harper ;,;$17.41;,; blue ;,; 09/15/17, 
Michelle Howell ;,;$28.59;,; blue;,;   09/15/17   , 
Carroll Boyd;,; $14.51;,;   purple&blue   ;,;   
09/15/17   , Teresa Carter   ;,; $19.64 ;,; 
white;,;09/15/17   ,   Jacob Kennedy ;,; $11.40   
;,; white&red   ;,; 09/15/17, Craig Chambers;,; 
$8.79 ;,; white&blue&red   ;,;09/15/17   , Peggy Bell;,; $8.65 ;,;blue   ;,; 09/15/17,   Kenneth Cunningham ;,;   $10.53;,;   green&blue   ;,; 
09/15/17   ,   Marvin Morgan;,;   $16.49;,; 
green&blue&red   ;,;   09/15/17 ,Marjorie Russell 
;,; $6.55 ;,;   green&blue&red;,;   09/15/17 ,
Israel Cummings;,;   $11.86   ;,;black;,;  
09/15/17,   June Doyle   ;,;   $22.29 ;,;  
black&yellow ;,;09/15/17 , Jaime Buchanan   ;,;   
$8.35;,;   white&black&yellow   ;,;   09/15/17,   
Rhonda Farmer;,;$2.91 ;,;   white&black&yellow   
;,;09/15/17, Darren Mckenzie ;,;$22.94;,;green 
;,;09/15/17,Rufus Malone;,;$4.70   ;,; green&yellow 
;,; 09/15/17   ,Hubert Miles;,;   $3.59   
;,;green&yellow&blue;,;   09/15/17   , Joseph Bridges  ;,;$5.66   ;,; green&yellow&purple&blue 
;,;   09/15/17 , Sergio Murphy   ;,;$17.51   ;,;   
black   ;,;   09/15/17 , Audrey Ferguson ;,; 
$5.54;,;black&blue   ;,;09/15/17 ,Edna Williams ;,; 
$17.13;,; black&blue;,;   09/15/17,   Randy Fleming;,;   $21.13 ;,;black ;,;09/15/17 ,Elisa Hart;,; $0.35   ;,; black&purple;,;   09/15/17   ,
Ernesto Hunt ;,; $13.91   ;,;   black&purple ;,;   
09/15/17,   Shannon Chavez   ;,;$19.26   ;,; 
yellow;,; 09/15/17   , Sammy Cain;,; $5.45;,;   
yellow&red ;,;09/15/17 ,   Steven Reeves ;,;$5.50   
;,;   yellow;,;   09/15/17, Ruben Jones   ;,; 
$14.56 ;,;   yellow&blue;,;09/15/17 , Essie Hansen;,;   $7.33   ;,;   yellow&blue&red
;,; 09/15/17   ,   Rene Hardy   ;,; $20.22   ;,; 
black ;,;   09/15/17 ,   Lucy Snyder   ;,; $8.67   
;,;black&red  ;,; 09/15/17 ,Dallas Obrien ;,;   
$8.31;,;   black&red ;,;   09/15/17,   Stacey Payne 
;,;   $15.70   ;,;   white&black&red ;,;09/15/17   
,   Tanya Cox   ;,;   $6.74   ;,;yellow   ;,; 
09/15/17 , Melody Moran ;,;   $30.84   
;,;yellow&black;,;   09/15/17 , Louise Becker   ;,; 
$12.31 ;,; green&yellow&black;,;   09/15/17 ,
Ryan Webster;,;$2.94 ;,; yellow ;,; 09/15/17 
,Justin Blake ;,; $22.46   ;,;white&yellow ;,;   
09/15/17,   Beverly Baldwin ;,;   $6.60;,;   
white&yellow&black ;,;09/15/17   ,   Dale Brady   
;,;   $6.27 ;,; yellow   ;,;09/15/17 ,Guadalupe Potter ;,;$21.12   ;,; yellow;,; 09/15/17   , 
Desiree Butler ;,;$2.10   ;,;white;,; 09/15/17  
,Sonja Barnett ;,; $14.22 ;,;white&black;,;   
09/15/17, Angelica Garza;,;$11.60;,;white&black   
;,;   09/15/17   ,   Jamie Welch   ;,; $25.27   ;,; 
white&black&red ;,;09/15/17   ,   Rex Hudson   
;,;$8.26;,;   purple;,; 09/15/17 ,   Nadine Gibbs 
;,;   $30.80 ;,;   purple&yellow   ;,; 09/15/17   , 
Hannah Pratt;,;   $22.61   ;,;   purple&yellow   
;,;09/15/17,Gayle Richards;,;$22.19 ;,; 
green&purple&yellow ;,;09/15/17   ,Stanley Holland 
;,; $7.47   ;,; red ;,; 09/15/17 , Anna Dean;,;$5.49 ;,; yellow&red ;,;   09/15/17   ,
Terrance Saunders ;,;   $23.70  ;,;green&yellow&red 
;,; 09/15/17 ,   Brandi Zimmerman ;,; $26.66 ;,; 
red   ;,;09/15/17 ,Guadalupe Freeman ;,; $25.95;,; 
green&red ;,;   09/15/17   ,Irving Patterson 
;,;$19.55 ;,; green&white&red ;,;   09/15/17 ,Karl Ross;,;   $15.68;,;   white ;,;   09/15/17 , Brandy Cortez ;,;$23.57;,;   white&red   ;,;09/15/17, 
Mamie Riley   ;,;$29.32;,; purple;,;09/15/17 ,Mike Thornton   ;,; $26.44 ;,;   purple   ;,; 09/15/17, 
Jamie Vaughn   ;,; $17.24;,;green ;,; 09/15/17   , 
Noah Day ;,;   $8.49   ;,;green   ;,;09/15/17   
,Josephine Keller ;,;$13.10 ;,;green;,;   09/15/17 ,   Tracey Wolfe;,;$20.39 ;,; red   ;,; 09/15/17 ,
Ignacio Parks;,;$14.70   ;,; white&red ;,;09/15/17 
, Beatrice Newman ;,;$22.45   ;,;white&purple&red 
;,;   09/15/17, Andre Norris   ;,;   $28.46   ;,;   
red;,;   09/15/17 ,   Albert Lewis ;,; $23.89;,;   
black&red;,; 09/15/17,   Javier Bailey   ;,;   
$24.49   ;,; black&red ;,; 09/15/17   , Everett Lyons ;,;$1.81;,;   black&red ;,; 09/15/17 ,   
Abraham Maxwell;,; $6.81   ;,;green;,;   09/15/17   
,   Traci Craig ;,;$0.65;,; green&yellow;,; 
09/15/17 , Jeffrey Jenkins   ;,;$26.45;,; 
green&yellow&blue   ;,;   09/15/17,   Merle Wilson 
;,;   $7.69 ;,; purple;,; 09/15/17,Janis Franklin   
;,;$8.74   ;,; purple&black   ;,;09/15/17 ,  
Leonard Guerrero ;,;   $1.86   ;,;yellow  
;,;09/15/17,Lana Sanchez;,;$14.75   ;,; yellow;,;   
09/15/17   ,Donna Ball ;,; $28.10  ;,; 
yellow&blue;,;   09/15/17   , Terrell Barber   ;,; 
$9.91   ;,; green ;,;09/15/17   ,Jody Flores;,; 
$16.34 ;,; green ;,;   09/15/17,   Daryl Herrera 
;,;$27.57;,; white;,;   09/15/17   , Miguel Mcguire;,;$5.25;,; white&blue   ;,;   09/15/17 ,   
Rogelio Gonzalez;,; $9.51;,;   white&black&blue   
;,;   09/15/17   ,   Lora Hammond ;,;$20.56 ;,; 
green;,;   09/15/17,Owen Ward;,; $21.64   ;,;   
green&yellow;,;09/15/17,Malcolm Morales ;,;   
$24.99   ;,;   green&yellow&black;,; 09/15/17 ,   
Eric Mcdaniel ;,;$29.70;,; green ;,; 09/15/17 
,Madeline Estrada;,;   $15.52;,;green;,;   09/15/17 
, Leticia Manning;,;$15.70 ;,; green&purple;,; 
09/15/17 ,   Mario Wallace ;,; $12.36 ;,;green ;,; 
09/15/17,Lewis Glover;,;   $13.66   ;,;   
green&white;,;09/15/17,   Gail Phelps   ;,;$30.52   
;,; green&white&blue   ;,; 09/15/17 , Myrtle Morris 
;,;   $22.66   ;,; green&white&blue;,;09/15/17"""

#------------------------------------------------
# Start coding below!
# replacing an element
daily_sales_replaced = daily_sales.replace(';,;',',')
print(daily_sales_replaced)
daily_transactions = daily_sales_replaced.split(',')

print(daily_transactions)

#appending elements to new list
daily_transactions_split = []
for i in daily_transactions:
  daily_transactions_split.append(i.split(','))
  
print(daily_transactions_split)

#iterating through a 2d list in order to eleminate white space, and appending to a new list
transactions_clean = []
#double for-loop iterates through a 2d list.
for list in daily_transactions_split:
  for transactions in list:
    transactions_clean.append(transactions.strip(' '))
    
print(transactions_clean)


customers = []
sales = []
thread_sold = []

#Now, iterate through transactions_clean and for each transaction:
# 1. Append the customers name to customers.
# 2. Append the amount of the sale to sales.
# 3. Append the threads sold to thread_sold.


    

    












    














