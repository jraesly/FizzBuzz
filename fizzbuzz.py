def FizzBuzz():
	for b in range(1,101):
		if b % 3 == 0 and b % 5 == 0:
			print("FizzBuzz")
		elif b % 5 == 0:
			print("Buzz")
		elif b % 3 == 0:
			print("Fizz")
		else:
			print(b)

print(FizzBuzz())

