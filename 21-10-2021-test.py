'''
Program1: write a program which will take an integer N, which is the number of test cases.
Next N lines will take the integer.
You have to find out the (i)th fibbonacci number for each N. And after that find out the gcd of the output and print the one integer that is gcd 
For example 
Sample input:
3
3
2
4
Output:
1
Explanation:
3#number of test cases 
F(3)=2 # 3rd fibbonacci number 
F(2)=1#2nd fibbonacci number 
F(4)=3# 4th fibbonacci number 
Gcd of (2,1,3)=1#output
'''
a=int(input("Enter the number :"))
fact = 0                                         
series = 1                                      
if (a <= 0):
    print("The fibnacci series is", fact)
else:
    print(fact, series, end = " ")
    for i in range(2, a):
        new = fact + series                           
        print(new, end = "  ")
        fact = series
        series = new

def isGcdNum(num, val):
    while(num != val):
        if(num > val):
            num -= val
        else:
            val -= num
    return val
print(isGcdNum(54, 24))
print(isGcdNum(5, 15))


    
