# p=[3,5,7,"peter",34.56,[9,10,11]]
# p[0]=4 #let p[0] =4
# print(p)


# x=5
# y='ABC'
# z=[x,y]
# seq=[x,y,z]
# print(seq)

# seq=[x,y,z]
# print()
# x=0
# y=10
#
# print(seq)

# t=['a','b','c','d','e','f']
# del t[1]
# print(t)

# result=[]
# val=0
# while val>=0:
#     val=int(input('enter integer,-1 to quit'))
#     if val==-1:
#         break
#     result=result+[val]
# print(result)

def increment(x):
    print('beg of exec of increment x =', x)
    x+=1
    print('ending exex of increment x=',x)

x=5
print('before inc x =',x)
increment(x)
print('after incr x=',x)