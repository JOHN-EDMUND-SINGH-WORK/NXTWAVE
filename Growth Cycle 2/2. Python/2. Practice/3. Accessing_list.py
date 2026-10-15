""" Accessing Nested Lists
40/40
Solved
For this problem, the prefilled code will contain a list of tuples. Write a program to create a list with the values at the given indexes.
Input

The first line of input will contain a positive integer (N).
The next N lines will contain two space-separated integers.
The first number will be the index of the tuple.
The second number will be the index of the value in the tuple.
Output

The output should be a single line containing the list of values in the order of inputs given.
Explanation

For example, if the given N is 3, then read the inputs in the next three lines. If the inputs in the next three lines are
1 2
0 3
0 1

The value at index 2 in the tuple at index 1 in the list is 'hockey', similarly the output list should contain the values at given indexes. So the output should be
['hockey', 'grapes', 'banana']
Sample Input 1
3
1 2
0 3
0 1
Sample Output 1
['hockey', 'grapes', 'banana']
Sample Input 2
4
0 0
0 2
1 2
1 1
Sample Output 2
['apple', 'orange', 'hockey', 'football'] """ 
list_a = [('apple', 'banana', 'orange', 'grapes'), ('cricket', 'football', 'hockey'), ('car', 'bicycle', 'bus')]
# Write your code here
n=int(input())
c=[]
for i in range(n):
    a,b=tuple(map(int,input().split()))
    a,b=int(a),int(b)
    values=list_a[a][b]
    c.append(values)
print(c)