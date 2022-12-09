def matrix(n):
    m = [[0 for x in range(n)]
                      for y in range(n)]
    i = n / 2
    j = n - 1
    num = 1
    while num <= (n * n):
        if i == -1 and j == n:
            j = n - 2
            i = 0
        else:
            if j == n:
                j = 0
            if i < 0:
                i = n - 1
        if m[int(i)][int(j)]:
            j = j-2
            i = i+1
            continue
        else:
            m[int(i)][int(j)] = num
            num = num + 1
        j = j + 1
        i = i - 1
    
    for i in range(0, n):
        for j in range(0, n):
            print('%2d ' % (m[i][j]),end = '')
            if j == n - 1:
                print()
    print ("Sum of eggs in each row or column and diagonal =",n * (n * n + 1) / 2, "\n")
def EvenNumbers(n):
    arr = [[(n * y) + x + 1 for x in range(n)] for y in range(n)]
    for i in range(0, n // 4):
        for j in range(0, n // 4):
            arr[i][j] = (n * n + 1) - arr[i][j];

    for i in range(0, n // 4):
        for j in range(3 * (n // 4), n):
            arr[i][j] = (n * n + 1) - arr[i][j];

    for i in range(3 * (n // 4), n):
        for j in range(0, n // 4):
            arr[i][j] = (n * n + 1) - arr[i][j];


    for i in range(3 * (n // 4), n):
        for j in range(3 * (n // 4), n):
            arr[i][j] = (n * n + 1) - arr[i][j];


    for i in range(n // 4, 3 * (n // 4)):
        for j in range(n // 4, 3 * (n // 4)):
            arr[i][j] = (n * n + 1) - arr[i][j];


    for i in range(n):
        for j in range(n):
            print('%2d ' % (arr[i][j]), end=" ")
        print()
    print ("Sum of eggs in each row or column and diagonal =",n * (n * n + 1) / 2, "\n")

n = int(input(
    "please enter a number : "
))
if n%2==0:
    EvenNumbers(n)
else:
    matrix(n)



