#!/bin/bash

echo "bash script execution successful..."

#working with variables;

	initial='inititial variable access execution successful...'

#accessing variables; $example_variable

	echo $initial

#conditionals; if [], then, else, fi

#comparison operators; equal = (-eq), not equal = (-nq), less than or equal = (-le)

#comparison operators; less than = (-lt), greater than or equal = (-ge), 

#greater than = (-gt), is null = (-z)

#comparing strings; equals = (==), not equal = (!=). if ["$foo" == "$bar"] 


	less_than_one="the number is less than 1"

	equal_to_one="the number is equal to 1"

	instance=1

if [ $instance -lt 1 ]
then 
  echo $less_than_one
else 
  echo $equal_to_one 
fi 

echo "Please enter your name: "
read name
echo -e "Hello $name!"


