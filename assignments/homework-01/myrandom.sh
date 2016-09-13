
#!/bin/bash
#path to the file to be read where the dictionary words are located
path="/usr/share/dict/words"
#calculating count of words in file
count=$( cat "$path" | wc -l )
#random generation from  word count
randomnum=$((RANDOM%$count+1))
#generates a random word from the file
sed -n "$randomnum p" $path;

