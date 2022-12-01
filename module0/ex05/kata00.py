kata = (19, 42, 21)

if __name__ == '__main__':
	print(f"The {len(kata)} numbers are: %s" % str(kata).replace("(", "").replace(")", ""))

