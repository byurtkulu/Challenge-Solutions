def fib(n):
    lst = [None]*(n+1);
    if n == 0:
        print 0
        return
    if n == 1:
        print 1
        return
    lst[0] = 0
    lst[1] = 1
    
    for i in range(2, n+1):
        lst[i] = lst[i-1] + lst[i-2]
    
    print lst[n]
    return
    
while(raw_input):
    try:
        n = int(raw_input())
        fib(n)
    except EOFError:
        break