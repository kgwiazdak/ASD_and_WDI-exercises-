from cmath import inf


def Matrix_chain_multiplication(p):
    n = len(p)-1
    m=[[0 for _ in range(n)]for _ in range(n)]
    for l in range(2,n+1):
        for i in range(1,n-l+2):
            j = 1+l-1
            m[i][j]=inf
            for k in range(i, j):
                q = m[i][k]+m[k+1][j]+p[i-1][0]*p[k][1]*p[j][]
                if q<m[i][j]:
                    m[i][j]=q
    return m[0][n-1]

if __name__ == '__main__':
    p = [[30,35], [35,15],[15,5],[5,10], [10,20],[20,25]]
    print(Matrix_chain_multiplication(p))