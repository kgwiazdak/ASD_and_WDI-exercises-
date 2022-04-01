def prime(number):
    from math import sqrt
    if number==2 or number==3 or number==5 or number==7:
        return True
    if number%2==0 or number%3==0 or number%5==0 or number<2:
        return False
    for i in range(3, int(sqrt(number)), 2):
        if number%i==0:
            return False
    return True

counter = 0

def exe17(n1, n2):

    l1 = str(n1)
    l2 = str(n2)

    def rek(l1,l2,ending = '', n=0):
        global counter
        ending = l2[:n]+l1+l2[n:]
        if prime(int(ending)):
            counter+=1

        if n==len(l2):
            return False


        return rek(l1,l2,ending, n+1)

    rek(l1,l2)






if __name__ == '__main__':
    exe17(131717, 11731)
    print(counter)
