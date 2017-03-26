#!/bin/python3

import sys
s = input().strip()
count=0
if s!='':
    count=1
    temp=''
    if(s[0].islower()):
        temp="lower"
    else:
        temp="upper"
    for letter in s:
        if(letter.islower()):
            new="lower"
        else:
            new="upper"
        if (new is "upper"):
            count=count+1
            temp=new
print(count)