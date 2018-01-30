def recurrance(n, k):
    #basic fibbonnaci recurrance
    if n == 1:
        return 1
    elif n == 2:
        return k
    firstGeneration = recurrance(n - 1, k)
    secondGeneration = recurrance(n - 2, k)
    # does not follow fibbonnaci perfectly!
    # number of adults last generation == number of rabbits 2 generations back
    # multiply that by k, get number of rabbits born.
    # add number of rabbits present last generation.
    if n <= 4:
        return firstGeneration + secondGeneration
    return firstGeneration + secondGeneration * k

#call function
print(recurrance(28,4))
