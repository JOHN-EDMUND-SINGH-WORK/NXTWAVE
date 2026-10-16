""" Lower Triangle
65/65
Solved
For this problem, the prefilled code will contain an MxN matrix. Write a program to print the lower triangle of the matrix.
Lower triangular matrix is a matrix which contain elements below principle diagonal including principle diagonal elements.
Input

The first line of input will contain two space-separated integers, denoting the M and N.
The next M following lines will contain N space-separated integers, denoting the elements of each list.
Output

The output should be M rows containing the elements in the form of a lower triangle.
Explanation

For example, if the given M is 3 and N is 3, read the inputs in the next three lines. If the numbers given in the next three lines are the following.
1 2 3
10 20 30
5 10 15

The lower triangle of the above matrix is
[1]
[10, 20]
[5, 10, 15]
Sample Input 1
3 3
1 2 3
10 20 30
5 10 15
Sample Output 1
[1]
[10, 20]
[5, 10, 15]
Sample Input 2
2 5
-50 20 3 25 -20
88 17 38 72 -10
Sample Output 2
[-50]
[88, 17] """

first_input=list(map(int,input().split()))
row=first_input[0]
col=first_input[1]
matrix=[]
for i in range(row):
    list1=list(map(int,input().split()))
    matrix.append(list1)
    print(matrix)

for j in range(len(matrix)):
    list2=matrix[j][:j+1]
    print(list2)