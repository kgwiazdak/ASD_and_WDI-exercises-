def shortening(l,m):
    for i in range (2,l+1):
        while l%i==0 and m%i==0:
                l=l//i
                m=m//i
    return (l,m)


if __name__ == '__main__':
    print(shortening(6, 120))