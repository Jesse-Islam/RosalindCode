

def fib(i, j):
    gen = [1, 1]
    #gen.append(unlist([0]*(i+1)))
    generations=[]
    generations=gen+([0]*i)
    #print(generations)
    count = 2 
    while (count < i):
        if (count < j):
            generations[count]=generations[count-2] + generations[count-1]
           # print(generations[count])
        elif (count == j or count == j+1):
            generations[count]=generations[count-2] + generations[count-1] - 1
        else:
            generations[count]=generations[count-2] + generations[count-1] - generations[count-(j+1)]
        count =count + 1                                                      
    return (generations[count-1])



n, m = 90,17

print (fib(n, m))
