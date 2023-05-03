#number=int(input("Enter a range: "))
number=100
for i in range(1,number):
        if(i%3==0 and i%5==0):
            print(f"[{i}]: Fizzbuzz")
        elif(i%5==0):
            print(f"[{i}]: Buzz")
        elif(i%3==0):
            print(f"[{i}]: Fizz")