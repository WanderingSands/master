#!/bin/bash

#file="~/master/linux/pagenum.txt"
#number=$(cat $"pagenum.txt")
echo "What page are you on?"
read pagenum
echo "How many readable pages are there in the book you are going though?"
read number
echo "You have $(($number-$pagenum)) pages to go."
