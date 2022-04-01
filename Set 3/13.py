tablica = []

def exe13(number, n=1, suma = 0, memory=[]):
    if suma==number:
        tablica.append(memory)
        return True
    if n>=number or suma>number:
        return False

    mem = memory.copy()
    mem.append(n)
    return exe13(number, n, suma + n, mem) | exe13(number, n + 1, suma, memory)

if __name__ == '__main__':
    exe13(13)
    for element in tablica:
        print(element)
