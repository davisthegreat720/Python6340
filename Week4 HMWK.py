# def fun2(stars):
#     for m in range(stars +1):
#         print(end="*")
#     print()
#
# fun2(5)
# fun2(0)
# fun2(-2)

def proc(n):
    if n < 1:
        return 1
    else:
        return proc(n/2) + proc(n-1)
print(proc(0))
print(proc(1))