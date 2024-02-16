print ("hello world")
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
	
print (isPrime(0))


