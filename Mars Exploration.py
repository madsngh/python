'''Sami's spaceship crashed on Mars! She sends  sequential SOS messages to Earth for help.

NASA_Mars_Rover.jpg

Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, , determine how many letters of Sami's SOS have been changed by radiation.

Input Format

There is one line of input: a single string, .

Note: As the original message is just SOS repeated  times, 's length will be a multiple of .

Constraints

 will contain only uppercase English letters.
Output Format

Print the number of letters in Sami's message that were altered by cosmic radiation.

Sample Input 0

SOSSPSSQSSOR
Sample Output 0

3
Sample Input 1

SOSSOT
Sample Output 1

1
Explanation

Sample 0

 = SOSSPSSQSSOR, and signal length . Sami sent  SOS messages (i.e.: ).

Expected signal: SOSSOSSOSSOS
Recieved signal: SOSSPSSQSSOR

We print the number of changed letters, which is 3.

Sample 1

 = SOSSOT, and signal length . Sami sent  SOS messages (i.e.: ).

Expected Signal: SOSSOS
Received Signal: SOSSOT

We print the number of changed letters, which is 1.
Submissions: 4814
Max Score: 15
Difficulty: Easy
Rate This Challenge:

More
Current Buffer (saved locally, editable)     '''
#!/bin/python3
S = input().strip()
count=str(S).__len__()%3
b=0
n=3
while True:
    word=S[int(b):int(n)]
    b=n
    if(n>str(S).__len__()):
        break
    else:
        if word[0]!='S':
            count=count+1
        if word[1]!='O':
            count = count + 1
        if word[2]!='S':
            count=count+1
        print(word)
    n = n + 3
print(count)