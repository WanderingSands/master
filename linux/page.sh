#!/bin/bash

file="~/master/linux/pagenum.txt"
number=$(cat $"pagenum.txt")
echo "What page are you on?"
read pagenum

echo "You have $(($number-$pagenum)) pages to go."
