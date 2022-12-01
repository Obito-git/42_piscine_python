import sys

if __name__ == '__main__':
	if len(sys.argv) == 1:
		sys.exit("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
	if len(sys.argv) != 3:
		sys.exit("AssertionError: wrong arguments count")
	try:
		a = int(sys.argv[1])
		b = int(sys.argv[2])
	except ValueError:
		sys.exit("AssertionError: only integers")
	print(f"Sum:\t\t{a + b}")
	print(f"Difference:\t{a - b}")
	print(f"Product:\t{a * b}")
	try:
		print(f"Quotient:\t{a / b}")
	except ZeroDivisionError:
		print("Quotient:\tERROR (division by zero)")
	try:
		print(f"Remainder:\t{a % b}")
	except ZeroDivisionError:
		print(f"Remainder:\tERROR (modulo by zero)")
