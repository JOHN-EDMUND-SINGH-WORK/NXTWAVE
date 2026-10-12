""" List of Maximum Values
40/40
Solved
Write a program to create a list with maximum values in each list.
Input

The first line of input will contain a positive integer N.
The next N lines will contain space-separated integers.
Output

The output should be a single line containing the list of maximum values in each list.
Explanation

For example, if the given N is 3, read the inputs in the next three lines.
If the given three strings are as the following.
1 2 3 4
10 20 30
5 10 15 20

Your code should print the list of maximum values in each list.
So the output should be
[4, 30, 20]
Sample Input 1
3
1 2 3 4
10 20 30
5 10 15 20
Sample Output 1
[4, 30, 20]
Sample Input 2
4
-50 20 3
88 17
3 11
200 1800
Sample Output 2
[20, 88, 11, 1800] """

n=int(input())
c=[]
for i in range(n):
    a=list(map(int,input().split()))
    b=max(a)
    c.append(b)
print(c)