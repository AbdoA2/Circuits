from copy import deepcopy

class Matrix:
    def __init__(self, m, n):
        self.n = n
        self.m = m
        self.matrix = [[i * 0 for i in range(n)] for j in range(m)]

    def __add__(self, other):
        if other.n != self.n or other.m != self.m:
            raise ArithmeticError

        ans = Matrix(self.m, self.n)
        ans.matrix = [[sum(d) for d in zip(self.matrix[i], other.matrix[i])] for i in range(self.m)]

        return ans

    def __sub__(self, other):
        if other.n != self.n or other.m != self.m:
            raise ArithmeticError

        ans = Matrix(self.m, self.n)
        ans.matrix = [[d[0] - d[1] for d in zip(self.matrix[i], other.matrix[i])] for i in range(self.m)]

        return ans

    def __mul__(self, other):
        if self.n != other.m:
            raise ArithmeticError

        ans = Matrix(self.m, other.n)
        for i in range(self.m):
            for j in range(other.n):
                for k in range(self.n):
                    ans.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]

        return ans

    def __str__(self):
        return "\n".join(" ".join(map(str, self.matrix[i])) for i in range(self.m))

    def __LUP_Decomposition(self, A, n):
        for k in range(n):
            p = 0; k_ = 0; i = 0
            for i in range(k, n, 1):
                if abs(A[i][k]) > p:
                    p = abs(A[i][k])
                    k_ = i
            if p == 0:
                print('Error: Singular Matrix')
                return
            for i in range(n+1):
                A[k][i], A[k_][i] = A[k_][i], A[k][i]
            for i in range(k+1, n, 1):
                A[i][k] /= A[k][k]
                for j in range(k+1, n, 1):
                    A[i][j] -= A[i][k] * A[k][j]


    def __LUP_Solve(self, A, n):
        s = lambda l, y: sum(l[i] * y[i] for i in range(len(l)))
        y = [0]*n
        for i in range(n):
            y[i] = A[i][n] - s(y[:i], A[i][:i])
        x = [0]*n
        for i in range(n-1, -1, -1):
            x[i] = (y[i] - s(x[i+1:], A[i][i+1:-1]))/A[i][i]
        return x

    def solve(self):
        if self.n != self.m + 1:
            raise ArithmeticError

        A = deepcopy(self.matrix)
        self.__LUP_Decomposition(A, self.n - 1)
        x = self.__LUP_Solve(A, self.n - 1)
        return x