#!/bin/bash
#assigning the count of the arguments to a variable
number=$#
sum=0
#the loop to calculate the sum of the arguments
if [ $number -le 9 ]
then
#sending all the argument values into an array
myarray=("$@")
for (( i=0; i<${number}+1; i++ ));
do
   sum=$((${myarray[i]} + $sum))
done
#the print statements
for (( i=0;i<${number}-1; i++ ));
do
printf "${myarray[i]}+" 
done
printf "${myarray[$number-1]}"
printf "="$sum 
else
echo too many arguments
fi
