import time
from time import sleep


def ft_progress(lst):
	one_percent = int(len(lst) / 100)
	curr_pos = 0
	percent = 0
	if not lst:
		yield None
	start_time = time.time()
	for elem in lst:
		curr_pos += 1
		try:
			if curr_pos % one_percent == 0 and percent < 100:
				percent += 1
		except ZeroDivisionError:
			percent = 100
		elapsed_time = time.time() - start_time
		if percent != 0:
			eta = (elapsed_time * 100 / percent) - elapsed_time
		else:
			eta = 0
		print(f"ETA: {eta:5.2f} [{percent:3}%] [{'=' * int(percent / 5) + '>':<20.20}] elapsed time {elapsed_time:.2f}s", end="\r")
		yield elem


if __name__ == '__main__':
	listy = range(3333)
	ret = 0
	for elem in ft_progress(listy):
		ret += elem
		sleep(0.005)
	print()
	print(ret)
