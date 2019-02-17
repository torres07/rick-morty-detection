#bin/bash

cd txt;

a=1
for i in *; do
  new=$(printf "morty-yolo_%d.txt" "$a") #04 pad to length of 4
  mv -i -- "$i" "$new"
  let a=a+1
done
