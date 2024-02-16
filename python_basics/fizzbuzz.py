
def isPrime(n):
	if n == 1 or n == 0:
		return False
	elif n == 2:
		return True
	else:
		for x in range(2,n):
			if n % x == 0:
				return False
		
		return True


def oneToHundred():
	for i in range (1,100):
		if isPrime(i):
			print(f" {i} prime")
		elif i % 15 == 0:
			print (f" {i} FizzBuzz")
		elif i % 5 == 0:
			print(f" {i} Buzz")
		elif i % 3 == 0:
				print(f" {i} Fizz")

#oneToHundred()
isPrime(1)