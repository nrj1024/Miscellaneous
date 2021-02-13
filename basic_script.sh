#!/bin/bash

echo "Enter the first num : "
read n1
echo "Enter the second num : "
read n2
((sum=n1+n2))
echo "The sum is : $sum"

if [ $n1 -gt $n2 ]
then
echo "$n1 is greater"
else
echo "$n2 is greater"
fi 
