def tobetri(n):
    k = ( n * (n + 1) ) / 2
    return int(k)
def checktri(n):
    li = []
    li.append(tobetri(n))
    for i in li:
        return i
def div(n):
    li = []
    k = checktri(n)
    print(k)
    for i in range(1,k):
        if k % i == 0:
            li.append(i)
    return len(li)
def count():
    for i in range(1200,1800):
        if div(i)==50:
            print(checktri(i))
print(div(12375))
