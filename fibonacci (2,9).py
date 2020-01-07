#Fibonocci numbers are defined as follows:

#Zeroth Fibonacci number F(0) is equal 0
#Second Fibonacci number F(1) is equal 1
#Third Fibonacci number F(2) is equal F(0) + F(1) is equal 1
...
#Nth Fibonacci number F(N) is equal F(N-1) + F(N-2)

#Given a nonegative integer N, print the N-th Fibonacci number F(N)

#For example, on input
#4
#output must be
#3

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

nth_num = int(input())

print(fibo(nth_num))
