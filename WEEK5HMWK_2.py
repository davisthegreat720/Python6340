def sum1(n):
    s = 0

    while n > 0:
        s += 1

        n -= 1

    return s


def sum2():
    global val

    s = 0

    while val > 0:
        s += 1

        val -= 1

    return s


def sum3():
    s = 0

    for i in range(val, 0, -1):
        s += 1

    return s


global val

val = 5

print(sum1(5))

print(sum2())

print(sum3())

#the answer is 5 5 0, a global value is defined as 5 , sum 1 defined function uses 5 and is asked to be printed sum2 and sum3 functions
#use the global value that is defined, I kinda get it but will need further explanation