#!/bin/bash
#assigning date format to a variable
d=$(date +%Y_%m_%d)
#reading the command line first argument
filename=$1
#appending the filename with date format
echo"">$d"_"$filename
