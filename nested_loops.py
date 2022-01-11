#!/usr/bin/env python3
#nested loops
#loops that list all 2d lists, 
#then adds each element within a nested loop.
embedded_numbers = [
    [5, 10],
    [15, 20], 
    [25, 30], 
    [35, 40],
    [45, 50]
]
#total count variable will be updated.
total_count = 0
#outer loop iterates and prints the elements within the 2d list.
for pairs in embedded_numbers:
    print(pairs)
    #inner loop iterates through every number within each pair.
    for int in pairs:
        #total count variable is updated by adding every int value
        #within each pair-sublist on every iteration
        #once the loop ends, the total count is printed out.
        total_count += int
print(total_count)


