"""
File: largest_digit.py
Name: Tina Hung
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	This function compares digits and finds the biggest one
	:param n: The number to find the biggest digit.
	:return: The biggest digit.
	"""
	# Make sure n is positive.
	if n < 0:
		n = -n
	max_num = n % 10
	return helper(n, max_num)


def helper(n, max_num):
	"""
	:param n: The number to find the biggest digit.
	:param max_num: Return value, the default is the last digit of the number.
	:return: max_num
	"""
	if n == 0:		# Base case
		return max_num
	# If the digit is 9, it is already the biggest digit from 0 to 9.
	elif n == 9:
		return 9
	else:
		if n % 10 > max_num:
			max_num = n % 10
		# To check the next digit of the number
		if n > 0:
			n //= 10
		return helper(n, max_num)

# 我原本的想法，跟高欣平討論過後改為上面的想法
# def helper(n, max_num, run_times, sec_times):
#
# 	if (sec_times == run_times and run_times != 0) or (run_times == 0 and sec_times != 0):
# 		return max_num
# 	elif n == 9:
# 		return 9
# 	elif n < 10:
# 		if n > max_num:
# 			max_num = int(n)
# 		n *= 10
# 		sec_times += 1
# 		return helper(n % 10, max_num, run_times, sec_times)
# 	else:
# 		n /= 10
# 		run_times += 1
# 		return helper(n, max_num, run_times, sec_times)



if __name__ == '__main__':
	main()
