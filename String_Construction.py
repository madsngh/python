'''Amanda has a string, , of  lowercase letters that she wants to copy into a new string, . She can perform the following operations any number of times to construct string :

Append a character to the end of string  at a cost of  dollar.
Choose any substring of  and append it to the end of  at no charge.
Given  strings (i.e., ), find and print the minimum cost of copying each  to  on a new line.

Input Format

The first line contains a single integer, , denoting the number of strings.
Each line  of the  subsequent lines contains a single string, .

Constraints

Subtasks

 for  of the maximum score.
Output Format

For each string  (where ), print the minimum cost of constructing string  on a new line.

Sample Input

2
abcd
abab
Sample Output

4
2
Explanation

Query 0: We start with  and .

Append character '' to  at a cost of  dollar, .
Append character '' to  at a cost of  dollar, .
Append character '' to  at a cost of  dollar, .
Append character '' to  at a cost of  dollar, .
Because the total cost of all operations is  dollars, we print  on a new line.

Query 1: We start with  and .

Append character '' to  at a cost of  dollar, .
Append character '' to  at a cost of  dollar, .
Append substring  to  at no cost, .
Because the total cost of all operations is  dollars, we print  on a new line.

Note

A substring of a string  is another string  that occurs "in"  (Wikipedia). For example, the substrings of the string "abc" are "a", "b" ,"c", "ab", "bc", and "abc"'''
#!/bin/python3

import sys


n = int(input().strip())
l=[]
cost=[]
for a0 in range(n):
    s = input().strip()
    l.append(s)
for words in l:
    local_cost = 0
    m=[]
    for char in words:
        if not(char in m):
            m.append(char)
            local_cost=local_cost+1


    cost.append(local_cost)
for price in cost:
    print(price)