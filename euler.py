import helper
import math

def problem23 () : #Non-abundant sums
    sum,abun = 276,[12,16,18,20] #sum 1...23
    for i in range (24,28124) :
        yup = True
        if (helper.sum_divisors(i) > i) : abun.append(i)
        for j in abun :
            if (i-j in abun) : yup = False
        if yup : sum += i
    return sum

def problem22() : #Names scores
    sum,count = 0,1
    names = open('names.txt','r')
    lines = names.read().split(',')
    lines.sort()
    for i in lines :
        sum += count*helper.alphaval(i[1:len(i)-1])
        count += 1
    return sum

def problem21() : #Amicable numbers
    lst,sum = [],0
    for i in range (1,10000) :
        j = helper.divisors(i)
        if (j != i and helper.sum_divisors(j) == i) :
            if (j not in lst) :
                lst.append(i)
                lst.append(j)
    for x in lst : sum+=x
    return sum

def problem20() : #Factorial digit sum
    return helper.sumdigits(math.factorial(100))


def problem19() : #Counting Sundays
    days,acc = 366,0
    for y in range(1901,2001):
        for m in range(1,13):
            if (days%7==0): acc+=1
            days+=helper.days_in(m,y)
    return acc


def problem18() : #Maximum path sum I
    t=helper.triangle()
    def find (i,j):
        if (j==len(t)-1) :
            return t[j][i]
        else :
            return t[j][i] + max(find(i,j+1),find(i+1,j+1))
    return find (0,0)


def problem17() : #Number letter counts
    ones  = 3+3+5+4+4+3+5+5+4
    teens = 3+6+6+8+8+7+7+9+8+8
    tens  = 10*(6+6+5+5+5+7+6+6) + 8*ones
    hundreds = 100*ones+9*(ones+teens+tens)+7*9+9*99*10
    return ones+teens+tens+hundreds+11


def problem16() : #Power digit sum
    return helper.sumdigits(2**1000)


def problem15() : #Lattice paths
    a,b = 1,1
    for i in range (1,21):
        a *= (20+i)
        b *= i
    return a/b


def problem14() : #Longest Collatz sequence (slow but has to run 1 mil times)
    lst,m,c,d = range (1,1000001),0,0,{1:1}
    def collatz (n):
        if (n in lst): lst.remove(n)
        if (n not in d):
            if (n%2==0): d[n] = 1+collatz(n/2)
            else: d[n] = 1+collatz(3*n+1)
        return d[n]
    while (lst != []):
        t=lst[0]
        v=collatz(t)
        print t,v
        if (v>c):
            c=collatz(t)
            m=t
    return m


def problem13() : #Large sum
    acc = 0
    for i in helper.num50():
        acc += i
    return acc/10**42


def problem12() : #Highly divisible triangular number (is SUPER SLOW)
    def numdiv(n) :
        acc = 0
        for i in range (1,int(math.sqrt(n))+1):
            if (n % i == 0) :
                if (i*i==n) : acc +=1
                else : acc +=2
        return acc
    n = 1
    while (numdiv(n) <= 500) :
        return n,numdiv(n)
        n+=1
    return n


def problem11() : #Largest product in a grid
    def maxprod(h,u,d):
        n = 0
        for i in range (20-3*h):
            for j in range (3*u,20-3*d):
                lst = []
                for k in range (4):
                    lst.append(helper.grid()[j+k*(d-u)][i+k*h])
                n = max(n,helper.mulist(lst))
        return n
    return max(maxprod(1,0,0),maxprod(0,0,1),maxprod(1,1,0),maxprod(1,0,1))


def problem10() : #Summation of primes (is slow and brute force)
    acc,lst = 2,[2]
    for x in range(3,2000000):
        if helper.isprime(x,lst):
            lst.append(x)
            acc+=x
    return acc


def problem9() : #Special Pythagorean triplet
    for a in range(1,333):
        for b in range (a+1,(1000-a)/2+1):
            c = 1000-a-b
            if (a*a+b*b==c*c): return a*b*c


def problem8() : #Largest product in a series
    m,lst = 882,[7,3,1,6,7]
    for j in range (5,1000):
        lst = lst[1::]+[int(helper.strnum()[j])]
        m = max(m,helper.mulist(lst))
    return m


def problem7() : #10001st prime
    acc,n,primes = 1,2,[2]
    while (acc <10001):
        if (helper.isprime(n,primes)) :
            primes.append(n)
            acc+=1
        n+=1
    return primes[len(primes)-1]


def problem6() : #Sum square difference
    acc = 100*101/2
    for i in range(1,101): acc -= i*i
    return acc


def problem5() : #Smallest multiple
    return 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19


def problem4() : #Largest palindrome product
    n = 0
    for i in (range (100,1000))[::-1]:
        for j in (range (i,1000))[::-1]:
            if (str(i*j) == str(i*j)[::-1]): n = max(n,i*j)
    return n


def problem3() : #Largest prime factor
    def prime(n):
        i=2;
        while (n%i != 0 and i < n): i += 1
        if (i < n): prime (n/i)
        else: return n
    prime(600851475143)


def problem2() : #Even Fibonacci numbers
    a,b,c,acc = 0,1,1,0
    while (c<=4000000):
        if (c%2==0): acc+=c
        a=b;b=c;c=a+b
    return acc


def problem1() : #Multiples of 3 and 5
    acc = 0
    for i in range (1,1001):
        if (i%3==0 or i%5==0): acc +=i
    return acc