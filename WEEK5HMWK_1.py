def countdown(n):
    if n <= 0:

        print("stop")

    else:

        print(n)

        countdown(n - 1)


countdown(3)
#The answer is 3 2 1 stop
# countdown is a functional definition if n is less than or equal to 0 then the program will print "stop" otherwise
#it will print the number defined in n and subtract 1 until it gets to 0 then it will print stop