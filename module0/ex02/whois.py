import sys

if __name__ == "__main__":
	if len(sys.argv) != 2:
		sys.exit("One integer arg expected")
	try:
		res = int(sys.argv[1])
	except ValueError:
		sys.exit(sys.argv[1] + " is not integer number")
	if res == 0:
		print("I'm Zero")
	elif res % 2 == 0:
		print("I'm Even")
	else:
		print("I'm Odd")
