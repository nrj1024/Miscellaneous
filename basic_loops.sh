#!/bin/bash

echo "For loop"
for i in 1 2 3 4 5
do
echo $i
done
echo "For loop end"
echo

echo "While loop"
val=0
while [ $val -le 5 ]
do
echo "Value of val : $val"
((val=val+1))
done
echo "While loop end"
