#!/bin/bash
#assigning the variable with the required date format
d=$(date +_%Y_%m_%d)
#spliting the argument name using the command basename
file_name=$(basename "$1")
#extension being assigned to a variable
extension="${file_name##*.}"
filename="${file_name%.*}"
#creating the file
echo"">$filename"_"$d"."$extension
