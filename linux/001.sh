#!/bin/bash
#A simple script for my personal modification to the CLI's prompt.



PS1_OLD="$PS1"
PS1="\033[0;31m[\! \A \u@\h ./\W ]$\e[0m "
