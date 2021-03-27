#I am the fourth variant
from math import log,sin

def getFunctionValue(x_argument):
    return log(x_argument**2)+1-sin(x_argument)

def dichotomy(point1,point2,epsilon,count):
    delta = epsilon/4
    middlePoint = (point2+point1)/2


    if abs(point1 - point2)<epsilon:
        print("Iterations: ",count)
        return middlePoint

    x1 = middlePoint-delta
    x2 = middlePoint+delta
    f1 = getFunctionValue(x1)
    f2 = getFunctionValue(x2)


    if (f1>f2):
        count+=1
        return dichotomy(middlePoint,point2,epsilon,count)
    else:
        count+=1
        return dichotomy(point1,middlePoint,epsilon,count)


def golden_ratio(a, b, epsilon,count):
    count = 0

    x1 = a + 0.382 * (b - a)  # 1 - 1/ф
    x2 = b -  0.382 * (b - a)  # 1/ф

    fx1 = getFunctionValue(x1)
    fx2 = getFunctionValue(x2)
    while abs(a-b)>epsilon:

        count+=1
        if fx1<fx2:
            b = x2
            x2 = x1
            fx2 = fx1
            x1 = a + 0.382*(b-a)
            fx1 = getFunctionValue(x1)
        else:
            a = x1
            x1 = x2
            fx1 = fx2
            x2 = b - 0.382*(b-a)
            fx2  = getFunctionValue(x2)

    minX = (a + b) / 2
    print("Iterations: ",count)
    return minX

def Fib(n):
    if n == 1 or n==2: return 1
    return Fib(n-1)+Fib(n-2)

def fibonacci(a,b,n):
    x1 = a + (b-a)* Fib(n-2)/Fib(n)
    x2 = a + (b-a)* Fib(n-1)/Fib(n)
    fx1 = getFunctionValue(x1)
    fx2 = getFunctionValue(x2)
    print("Iterations: ", n)
    while n-1:
        if fx1<fx2:
            b = x2
            x2 = x1
            x1 = a + (b-x2)
            fx2 = fx1
            fx1 = getFunctionValue(x1)
        else:
            a = x1
            x1 = x2
            x2 = b - (x1-a)
            fx1 = fx2
            fx2 = getFunctionValue(x2)
        n-=1
    return (x1+x2)/2

def getParabolicAppMin(a,b,x2,fa,fb,fx2):

    return x2 - ((x2-a)**2*(fx2-fb)-(x2-b)**2*(fx2-fa))/(2*(x2-a)*(fx2-fb)-(x2-b)*(fx2-fa))

def parabolas(a,b,epsilon):
    fa = getFunctionValue(a)
    fb= getFunctionValue(b)
    x2 = (a+b)/2
    fx2 = getFunctionValue(x2)
    u=getParabolicAppMin(a,b,x2,fa,fb,fx2)
    count = 0
    len = abs(x2-u)
    while len>epsilon:
        prevuval = getFunctionValue(x2)
        uval = getFunctionValue(u)
        if uval<prevuval:
            b = x2
            fb = fx2
            x2 = u
            fx2 = uval
        else:
            a = u
            fa = uval
        count+=1
        print("Segment Length: ",abs(x2-u))
        u = getParabolicAppMin(a,b,x2,fa,fb,fx2)
    print("Iterations: ", count)
    return u

def combinedBrentMethod(func):
    pass

if __name__ == '__main__':
    print("Dichotomy")

    print(dichotomy(5,10,0.0005,0))

    print("Golden ratio")

    print(golden_ratio(5,10,0.0005,0))


    print("Fibbonacci")

    print(fibonacci(5,10,10))
    print("Parabolas")
    print(parabolas(5,10,0.005))

    print("Brent's Method")
