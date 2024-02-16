# def add(a,b=0,c=5):
#     x = a+b+c
#     return x
# print(add(10,3,7))

# def add(*p,**q):
#     print(p)
#     print(q)
 
# add(29,1,3,45,6, a=5,b=10,c=15,d=20)

month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
# tell weather a leap year or not

def is_leap(year):
   if  year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 'A leap year'
   else:
        return False
   # return no of days in that month in that year 
def days_in_month(year,month):
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month] 

#print(days_in_month(2022, 2))
#print(is_leap(2024))

y=20
def fun1(x):
    global y
    return x + y
# print(fun1(7))
# print(y)

def displayPerson(**kwargs):
    print(kwargs)
displayPerson(name="Emma", age=25)


def print_numbers(*args):
    print(args)
print_numbers(5, 23, 45, 78)

def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d
    return inner_fun(a, b)
   
    

res = outer_fun(5, 10)
# print(res)

def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d

    return inner_fun(a, b)
    return a

result = outer_fun(5, 10)
# print(result)

def fun():

 for i in range(1,5):
    print(i,end=' ')

# print(fun())

