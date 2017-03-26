'''Emma is playing a new mobile game involving  clouds numbered from  to . A player initially starts out on cloud , and they must jump to cloud . In each step, she can jump from any cloud  to cloud  or cloud .

There are two types of clouds, ordinary clouds and thunderclouds. The game ends if Emma jumps onto a thundercloud, but if she reaches the last cloud (i.e., ), she wins the game!

jump(1).png

Can you find the minimum number of jumps Emma must make to win the game? It is guaranteed that clouds  and  are ordinary-clouds and it is always possible to win the game.

Input Format

The first line contains an integer,  (the total number of clouds).
The second line contains  space-separated binary integers describing clouds .

If , the  cloud is an ordinary cloud.
If , the  cloud is a thundercloud.
Constraints

Output Format

Print the minimum number of jumps needed to win the game.

Sample Input 0

7
0 0 1 0 0 1 0
Sample Output 0

4
Sample Input 1

6
0 0 0 0 1 0
Sample Output 1

3
Explanation

Sample Case 0:
Because  and  in our input are both , Emma must avoid  and . Bearing this in mind, she can win the game with a minimum of  jumps: 4

jump(2).png

Sample Case 1:
The only thundercloud to avoid is . Emma can win the game in  jumps: 3
'''



n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
steps=0
num=0
while(num<=n-1):
    if(num+2<=n-1):
        if(c[num+2]!=1):
            num=num+2
            steps=steps+1
        else:
            if(c[num + 1] != 1):
                num = num + 1
                steps = steps + 1
    elif (num + 1 <= n - 1):
        if (c[num + 1] != 1):
            num = num + 1
            steps = steps + 1
    else:
        break
print(steps)