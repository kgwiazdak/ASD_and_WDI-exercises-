def king(n):

    def rek(w,k, skos1=[False for _ in range(2*n-1)], skos2=[False for _ in range(2*n-1)], normal = [-1 for _ in range(n)]):

        if w ==n:
            print(normal)
            print()
        if w==0 and k==n:
            return False

        if k==n:
            normal[w-1] = a
            normal[w-1]=-1
            skos2[w-2+n-q]=skos1[a+w-1]=False
            rek(w-1, a+1, skos1,skos2,normal)

        if k not in normal and skos2[n-1+w-k]==skos1[k+w]==False:
            normal[w]=k
            skos2[n-1+w-k]=skos1[k+w]=True
        else: rek(w,k+1, skos1, skos2, normal)

        return rek(w+1, 0, skos1, skos2, normal)

    for i in range(n):
        rek(0,i,n)


if __name__ == '__main__':
    n = 8
    king(n)