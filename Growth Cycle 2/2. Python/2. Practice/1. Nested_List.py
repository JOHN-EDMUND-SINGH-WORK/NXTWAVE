""" Nested List
40/40
Solved
Write a program to read N lines of inputs and create a nested list with each line as a list.
Input

The first line of input will contain a positive integer N.
The next N lines will contain space-separated integers.
Output

The output should be a single line containing the nested list.
Explanation

For example, if the given N is 3, read the inputs in the next three lines.
If the given three strings are as the following.
1 2 3 4
10 20 30
5 10 15 20

Your code should print the nested list with each line of input as a list in it.
So the output should be
[[1, 2, 3, 4], [10, 20, 30], [5, 10, 15, 20]]
Sample Input 1
3
1 2 3 4
10 20 30
5 10 15 20
Sample Output 1
[[1, 2, 3, 4], [10, 20, 30], [5, 10, 15, 20]]
Sample Input 2
4
-50 20 3
88 17
3 11
200 1800
Sample Output 2
[[-50, 20, 3], [88, 17], [3, 11], [200, 1800]] """

n=int(input())
a=[]
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
print(a)
