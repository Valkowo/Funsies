# I made this to calm the resentment I had for not knowing how to program back when I
# had to make an essay on the Collatz Conjecture. This has two parts: The first one to 
# get the graph of every iteration of n, and the last one to see the max values of the
# iterations a certain range of n gets. This is very optimizable, but I cannot bother.
# I'm 2 years late for this anyway.

import matplotlib.pyplot as plt

def Collatz(n):
    count=1
    max=0
    while(n!=1):
        if(n%2==0):
            n=n/2
        else:
            n=(3*n)+1
        count+=1
        if(max<n):
            max=n
    return [count,max]    #[steps, max value]

def progCollatz (n):
    if(n%2==0):
        n=n/2
    else:
        n=(3*n)+1
    return n

#To see the values every iteration gets for the input n

input=int(input("Enter a number: "))
aux=input
steps=0
while(aux!=1):
    aux=progCollatz(aux)
    steps+=1

x=[*range(steps)]
y=[*range(steps)]
aux=input
for i in range(steps):
    y[i]=progCollatz(aux)
    aux=y[i]
    
#To see the max values the series gets for every n in the range [1,n]

#ran=[*range(input("Enter a number")))]    

#for i in range(ran):
#    num=Collatz(i+1)
#    x[i]=int(i)
#    y[i]=int(num[1])

#Plot

plt.plot(x,y)
plt.xlabel("Steps")
plt.ylabel("Value")
plt.title("Value for every iteration of n="+str(input)+". Collatz Conjecture")
plt.show()
