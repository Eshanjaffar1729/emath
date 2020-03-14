import math
import random
import turtle

def ceil(x):
	return math.ceil(x)

def comb(n, k):
	return math.comb(n, k)

def copysign(x, y):
	return math.copysign(x, y)

def fabs(x):
	return math.fabs(x)

def factorial(x):
	return math.factorial(x)

def floor(x):
	return math.floor(x)

def fmod(x, y):
	return math.fmod(x, y)

def frexp(x):
	return math.frexp(x)

def fsum(iterable):
	return math.fsum(iterable)

def gcd(a, b):
	return math.gcd(a, b)

def isfinite(x):
	return math.isfinite(x)

def isinf(x):
	return math.isinf(x)

def isnan(x):
	return math.isnan(x)

def isqrt(n):
	return math.isqrt(n)

def ldexp(x, i):
	return math.ldexp(x, i)

def modf(x):
	return math.modf(x)

def perm(n, k=None):
	return math.perm(n, k=None)

def prod(iterable, *,start=1):
	return math.prod(iterable,start=1)

def remainder(x, y):
	return math.remainder(x, y)

def trunc(x):
	return math.trunc(x)

def exp(x):
	return math.exp(x)

def expm1(x):
	return math.expm1(x)

def log(x, base):
	return math.log(x, base)

def log1p(x):
	return math.log1p(x)

def log2(x):
	return math.log2(x)

def log10(x):
	return math.log10(x)

def pow(x, y):
	return math.pow(x, y)

def sqrt(x):
	return math.sqrt(x)

def acos(x):
	return math.acos(x)

def asin(x):
	return math.asin(x)
	
def atan(x):
	return math.atan(x)

def atan2(y, x):
	return math.atan2(y, x)

def cos(x):
	return math.cos(x)

def dist(p, q):
	return math.dist(p, q)

def hypot(*coordinates):
	return math.hypot(*coordinates)

def sin(x):
	return math.sin(x)

def tan(x):
	return math.tan(x)

def degrees(x):
	return math.degrees(x)
	
def radians(x):
	return math.radians(x)

def acosh(x):
	return math.acosh(x)

def asinh(x):
	return math.asinh(x)
	
def atanh(x):
	return math.atanh(x)

def cosh(x):
	return math.cosh(x)

def sinh(x):
	return math.sinh(x)
	
def tanh(x):
	return math.tanh(x)

def erf(x):
	return math.erf(x)

def erfc(x):
	return math.erfc(x)
	
def gamma(x):
	return math.gamma(x)

def lgamma(x):
	return math.lgamma(x)

def pi():
	return math.pi
	
def e():
	return math.e

def tau():
	return math.tau

def inf():
	return math.inf
	
def nan():
	return math.nan

#random related
def randrange(start, stop, step):
	return random.randrange(start, stop, step)

def randint(a, b):
	return random.randint(a, b)

##number theory related
def test_prime(x):
    li = []
    length = int(math.sqrt(x)) + 1
    for i in range(1,length):
        if x % i == 0:
            li.append(i)
    new_length = len(li)
    if new_length == 1:
        return True
    else:
        return False

def sum_prime_less_n(k):
    list_of_prime = []
    a             = 0
    for i in range(2,k):
        if test_prime(i):
            list_of_prime.append(i)
    for primes in list_of_prime:
        a += primes
    return a 

def n_prime(n):
    l = []
    x = n
    s = 2
    if n == 1:
        return 2
    else:
        while len(l) < n:
            for i in range(s, n**2):
                if test_prime(i):
                    l.append(i)
                if len(l) == n:
                    break
            x += 1
            result = l[-1]
        return result
    
def first_n_prime(n):
    l = []
    for i in range(1,n+1):
        l.append(n_prime(i))
    return l

def primes_less_n(n):
    list_of_prime = []
    a             = 0
    for i in range(2,n):
        if test_prime(i):
            list_of_prime.append(i)
    return list_of_prime

def sum_first_n_prime(n):
    l = []
    result = 0
    for i in range(1,n+1):
        l.append(n_prime(i))
    for primes in l:
        result += primes
    return result

##algebra related
def quad_root(a,b,c):
    D = (b**2) - 4*a*c
    if math.fabs(D) == D:
        Discriminant = math.sqrt(D)
        root1 = (-b + Discriminant)/2*a
        root2 = (-b - Discriminant)/2*a
        return root1,root2
    else:
        return "no real roots"

##geometry related
def square_area(x):
	return x**2

def rectangle_square(l,b):
	return l*b

def trapezium_area(a,b,h):
	return ((a+b)*h)/2

def circle_area(r):
	return math.pi * (r**2)

def circle_circumference(r):
	return math.pi*r*2

def square_diagonal(s):
	return 2*math.sqrt(s)

def rectangle_diagonal(l,b):
	return math.sqrt((l**2) + (b**2))

#geometry visualistaion
def draw_circle(r):
	turtle.circle(50)

def draw_square(s):
	for i in range(4):
		turtle.forward(s)
		turtle.right(90)

def draw_rectangle(l,b):
	turtle.forward(l)
	turtle.right(90)
	turtle.forward(b)
	turtle.right(90)
	turtle.forward(l)
	turtle.right(90)
	turtle.forward(b)


##intrest related
def simple_intrest(p,r,t):
	result = p*r*t/100
	return result

def compound_intrest(p,r,t):
	compound_intrest = p*((1+ (r/100))**t) - p
	return compound_intrest

#multiplication table
def mul_table(number,times):
	l = []
	for i in range(1,times):
		result = number*i
		string_result = " " + str(number) + " * " + str(i) + " = " + str(result)
		l.append(string_result)
	for items in l:
		print(items)

# ap
def n_term_ap(n,l):
	if len(l) < 3:
		return "pass atleast 3 numbers in the series"
	else:
		d  = l[1] - l[0]
		a  = l[0] 
		result = a + (n-1)*d
		return result

def sum_ap(n,l):
	if len(l) < 3:
		return "pass atleast 3 numbers in the series"
	else:
		d = l[1] - l[0]
		a = l[0]
		result = int((n/2)*(2*a + (n-1)*d))
		return result

#sequence generator
def fibo(x):
	l = [1,1]
	for i in range(x-2):
		l.append(l[i] + l[i+1])
	return l
