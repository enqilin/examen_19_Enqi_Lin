#fibonacci
"""xbonacci {1,1,1,1} 10 = {1,1,1,1,4,7,13,25,49,94}

xbonacci {0,0,0,0,1} 10 = {0,0,0,0,1,1,2,4,8,16}

xbonacci {1,0,0,0,0,0,1} 10 = {1,0,0,0,0,0,1,2,3,6}

xbonacci {1,1} produces the Fibonacci sequence"""

def xfibonacci(lista, n):
    lista2=[]
    for i in lista:
        lista2.append(i)
    for i in range(n-len(lista2)):
        lista2.append(sum(lista2[i:]))
    print(lista2)


if __name__ == '__main__':
    xfibonacci([1,1,1,1],10)
    xfibonacci([0,0,0,0,1],10)
    xfibonacci([1,0,0,0,0,0,1],10)
    xfibonacci([1,1],10)
