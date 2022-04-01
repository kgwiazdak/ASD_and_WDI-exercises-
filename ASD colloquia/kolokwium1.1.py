def multi(T):
    n = len(T)
    last =0
    for i in range(1, n//2+1): #ile liter ma się powtarzać
        word = T[0:i]
        m = i
        n = i*2
        n_word=T[m:n]
        counter=0
        while word==n_word:
            m=n
            n+=i
            n_word=T[m:n]
            counter+=1
        if counter>last:
            last=counter
    if last==0:
        return 0
    else:
        return last+1




