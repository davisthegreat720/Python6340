#i, j, and k are numbers
#(a) i is 3, j is 5, and k is 7
#(b) i is 3, j is 7, and k is 5

i=int(input("Enter a number for i?"))
j=int(input("Enter a Number for j?"))
k=int(input("Enter another number k?"))

if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k

print("i =", i, " j =", j, " k =", k)

# a)
# Enter a number for i? 3
# Enter a Number for j? 5
# Enter another number k? 7
# i = 5  j = 5  k = 7

# b)
# Enter a number for i? 3
# Enter a Number for j? 7
# Enter another number k? 5
# i = 3  j = 5  k = 5

#Gitupdate 1