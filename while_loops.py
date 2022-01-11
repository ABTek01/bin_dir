#!/usr/bin/env python3

#while loop will run a condition until it becomes false.
count = 0 #need to set a true condition so that way the loop executes/starts.
while count <= 10:
    print(f"{count}")
    count += 1
#any code written un-indented will run outside of loop.
print('loop end')

counter = 10
while counter >= 0:
    print(f"count is now: {counter}")
    counter -= 1
print('loop end')
    

#while loops and lists
#we need a way to know how many times we need our loop to 
#iterate based on the size of the collection.
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below:
#variable that tells the loop how many times it needs to run.
length = len(python_topics)

#need a variable to compare to length in order for loop to run.
index = 0
while index < length:
  print(F"I am learning about {python_topics[index]}")
  index += 1
print('I enjoy coding in python')
