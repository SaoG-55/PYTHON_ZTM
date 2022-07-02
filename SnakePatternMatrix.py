# User function Template for python3

class Solution:

    # Function to return list of integers visited in snake pattern in matrix.
    def snakePattern(self, matrix):
        # print(matrix)
        li = []
        for i in range(len(matrix)):
            if (i % 2 == 0):
                for j in range(len(matrix)):
                    # print(matrix[i][j],end=" ")
                    li.append(matrix[i][j])
            else:
                for j in range(len(matrix) - 1, -1, -1):
                    # print(matrix[i][j],end=" ")
                    li.append(matrix[i][j])
        return li

    # {




if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(values[k])
                k += 1
            matrix.append(row)
        obj = Solution()
        ans = obj.snakePattern(matrix)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends)

