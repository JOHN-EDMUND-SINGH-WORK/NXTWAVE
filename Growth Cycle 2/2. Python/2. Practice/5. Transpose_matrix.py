""" Transpose Matrix
65/65
Solved
For this problem, the prefilled code will contain an MxN matrix. Write a program to print the transpose of the matrix.
Transpose of a matrix is obtained by changing rows to columns and columns to rows.
Input

The first line of input will contain two space-separated integers, denoting the M and N.
The next M following lines will contain N space-separated integers, denoting the elements of each list.
Output

The output should be N lines containing the transpose of the given matrix.
Note: N is the length of a list in the matrix.
Explanation

For example, if the given M is 3 and N is 3, read the inputs in the next three lines. If the numbers given in the next three lines are the following.
1 2 3
10 20 30
5 10 15

By changing rows to columns and columns to rows, the transpose of the above matrix should be
[1, 10, 5]
[2, 20, 10]
[3, 30, 15]
Sample Input 1
3 3
1 2 3
10 20 30
5 10 15
Sample Output 1
[1, 10, 5]
[2, 20, 10]
[3, 30, 15]
Sample Input 2
2 5
-50 20 3 25 -20
88 17 38 72 -10
Sample Output 2
[-50, 88]
[20, 17]
[3, 38]
[25, 72]
[-20, -10] """
input1=list(map(int,input().split()))
m=input1[0]
n=input1[1]

matrix=[]

for i in range(m):
    row=list(map(int,input().split()))
    matrix.append(row)
print("----------Orginal Matrix----------")
for i in range(len(matrix)):
    print(matrix[i])

transpose=[]
for i in range(n):
    new_row=[]
    for j in range(m):
        new_row.append(matrix[j][i])
    transpose.append(new_row)

print("----------Transpose Matrix----------")
for i in range(len(transpose)):
    print(transpose[i])

