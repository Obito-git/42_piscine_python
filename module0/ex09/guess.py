import random

if __name__ == '__main__':
	numb = random.randint(1, 99)
	tries = 0
	print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret "
		"number.\nType 'exit' to end the game.\nGood luck!\n")
	while True:
		try:
			print("What's your guess between 1 and 99?")
			clientInput = input()
			if clientInput.lower() == "exit":
				print("Good bye!")
				break
			clientInput = int(clientInput)
			tries += 1
			if clientInput not in range(1, 100):
				print("The number is between 1 and 99")
			elif clientInput > numb:
				print("Too high!")
			elif clientInput < numb:
				print("Too low")
			else:
				if numb == 42:
					print("The answer to the ultimate question of life, the universe and everything is 42.")
				if tries == 1:
					print("Congratulations! You got it on your first try!")
				else:
					print("Congratulations, you've got it!")
					print(f"You won in {tries} attempts")
				break
		except EOFError:
			break
		except ValueError:
			print("That's not a number.")
